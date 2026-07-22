"""
Voice input module for Nova
Handles speech recognition and audio input
"""

import logging
import speech_recognition as sr

logger = logging.getLogger(__name__)


class VoiceInput:
    """Handle voice input and speech recognition"""
    
    def __init__(self, config):
        """
        Initialize voice input handler
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.recognizer = sr.Recognizer()
        self.microphone = None
        self.listening_timeout = config.get("voice", {}).get("listening_timeout", 10)
        
        # Initialize microphone
        self._init_microphone()
        
        logger.info("VoiceInput initialized")
    
    def _init_microphone(self):
        """Initialize microphone"""
        try:
            microphone_index = self.config.get("voice", {}).get("microphone_index", 0)
            self.microphone = sr.Microphone(device_index=microphone_index)
            logger.info(f"Microphone initialized at index {microphone_index}")
        except Exception as e:
            logger.warning(f"Error initializing microphone: {str(e)}")
            self.microphone = sr.Microphone()
            logger.info("Using default microphone")
    
    def listen(self):
        """
        Listen for audio input and convert to text
        
        Returns:
            str: Recognized text or empty string if not recognized
        """
        try:
            with self.microphone as source:
                logger.debug("Listening for audio...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(
                    source, 
                    timeout=self.listening_timeout,
                    phrase_time_limit=self.listening_timeout
                )
            
            # Try to recognize speech
            logger.debug("Recognizing speech...")
            text = self.recognizer.recognize_google(audio)
            logger.info(f"Recognized: {text}")
            return text
        
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return ""
        except sr.RequestError as e:
            logger.error(f"Error with speech recognition service: {str(e)}")
            return ""
        except sr.WaitTimeoutError:
            logger.debug("Listening timeout - no speech detected")
            return ""
        except Exception as e:
            logger.error(f"Error during listening: {str(e)}")
            return ""
    
    def list_microphones(self):
        """List available microphones"""
        try:
            for i, mic_name in enumerate(sr.Microphone.list_microphone_indexes()):
                logger.info(f"Microphone {i}: {mic_name}")
            return sr.Microphone.list_microphone_indexes()
        except Exception as e:
            logger.error(f"Error listing microphones: {str(e)}")
            return []
