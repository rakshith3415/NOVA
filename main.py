#!/usr/bin/env python3
"""
Nova - Local AI Voice Assistant
Main entry point for the application
"""

import os
import sys
import json
import time
import logging
from pathlib import Path

# Add modules to path
sys.path.insert(0, str(Path(__file__).parent))

from modules.voice_input import VoiceInput
from modules.ollama_handler import OllamaHandler
from modules.voice_output import VoiceOutput
from modules.command_executor import CommandExecutor
from modules.wake_word import WakeWordDetector
from utils.logger import setup_logging
from utils.helpers import load_config, save_config

# Setup logging
logger = setup_logging()

class Nova:
    """Main Nova Assistant class"""
    
    def __init__(self):
        """Initialize Nova assistant"""
        logger.info("Initializing Nova...")
        
        # Load configuration
        self.config = load_config()
        logger.info(f"Loaded config: {self.config.get('ollama', {}).get('model', 'default')}")
        
        # Initialize components
        self.voice_input = VoiceInput(self.config)
        self.ollama = OllamaHandler(self.config)
        self.voice_output = VoiceOutput(self.config)
        self.command_executor = CommandExecutor(self.config)
        self.wake_word_detector = WakeWordDetector(self.config)
        
        # State management
        self.running = False
        self.conversation_history = []
        
        logger.info("Nova initialized successfully")
    
    def process_command(self, user_input):
        """
        Process user command through Ollama and execute
        
        Args:
            user_input (str): User's voice command
            
        Returns:
            str: Nova's response
        """
        logger.info(f"Processing command: {user_input}")
        
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_input
        })
        
        try:
            # Get response from Ollama
            logger.debug("Querying Ollama...")
            response = self.ollama.query(user_input, self.conversation_history)
            
            # Add to conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            # Limit conversation history to last 10 messages
            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]
            
            # Try to execute system commands if detected
            self.command_executor.try_execute(user_input)
            
            logger.info(f"Response generated: {response[:100]}...")
            return response
            
        except Exception as e:
            logger.error(f"Error processing command: {str(e)}")
            error_response = f"Sorry, I encountered an error: {str(e)}"
            return error_response
    
    def listen_and_respond(self):
        """Listen for voice input and provide response"""
        try:
            logger.debug("Listening for voice input...")
            user_input = self.voice_input.listen()
            
            if not user_input:
                logger.warning("No speech detected")
                return
            
            logger.info(f"Heard: {user_input}")
            
            # Process the command
            response = self.process_command(user_input)
            
            # Speak the response
            logger.debug("Speaking response...")
            self.voice_output.speak(response)
            
        except Exception as e:
            logger.error(f"Error in listen_and_respond: {str(e)}")
            self.voice_output.speak("Sorry, I encountered an error processing your request.")
    
    def run(self):
        """Main loop for Nova"""
        self.running = True
        logger.info("Starting Nova main loop...")
        logger.info("Listening for wake word: 'Hey Nova'")
        
        try:
            while self.running:
                try:
                    # Listen for wake word
                    if self.wake_word_detector.detect():
                        logger.info("Wake word detected!")
                        self.voice_output.speak("I'm listening")
                        
                        # Listen and respond
                        self.listen_and_respond()
                    
                    # Small delay to prevent CPU spinning
                    time.sleep(0.1)
                    
                except KeyboardInterrupt:
                    logger.info("Keyboard interrupt detected")
                    break
                except Exception as e:
                    logger.error(f"Error in main loop: {str(e)}")
                    time.sleep(1)
        
        except Exception as e:
            logger.critical(f"Fatal error in run loop: {str(e)}")
        finally:
            self.shutdown()
    
    def shutdown(self):
        """Shutdown Nova gracefully"""
        logger.info("Shutting down Nova...")
        self.running = False
        self.voice_output.speak("Goodbye")
        logger.info("Nova shut down complete")
    
    def test_mode(self):
        """Test mode for debugging - accept text input instead of voice"""
        logger.info("Entering test mode (text input)")
        self.voice_output.speak("Test mode activated")
        
        try:
            while True:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    self.shutdown()
                    break
                
                if not user_input:
                    continue
                
                response = self.process_command(user_input)
                print(f"\nNova: {response}\n")
                self.voice_output.speak(response)
        
        except KeyboardInterrupt:
            self.shutdown()
        except Exception as e:
            logger.error(f"Error in test mode: {str(e)}")
            self.shutdown()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Nova - Local AI Voice Assistant")
    parser.add_argument("--test", action="store_true", help="Run in test mode (text input)")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument("--model", help="Specify Ollama model to use")
    
    args = parser.parse_args()
    
    # Enable debug logging if requested
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize Nova
    nova = Nova()
    
    # Override model if specified
    if args.model:
        logger.info(f"Using model: {args.model}")
        nova.config["ollama"]["model"] = args.model
    
    # Run in appropriate mode
    try:
        if args.test:
            nova.test_mode()
        else:
            nova.run()
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
