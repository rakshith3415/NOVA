"""
Voice output module for Nova
Handles text-to-speech and audio responses
"""

import logging
import pyttsx3
import threading

logger = logging.getLogger(__name__)


class VoiceOutput:
    """Handle voice output and text-to-speech"""
    
    def __init__(self, config):
        """
        Initialize voice output handler
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.voice_config = config.get("voice", {})
        self.engine = pyttsx3.init()
        
        # Configure TTS engine
        rate = self.voice_config.get("tts_rate", 150)
        volume = self.voice_config.get("tts_volume", 0.9)
        
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        
        # Set voice if available
        try:
            voices = self.engine.getProperty('voices')
            if voices:
                self.engine.setProperty('voice', voices[0].id)
                logger.info(f"TTS voice set to: {voices[0].name}")
        except Exception as e:
            logger.warning(f"Could not set voice: {str(e)}")
        
        logger.info("VoiceOutput initialized")
    
    def speak(self, text, async_mode=True):
        """
        Speak text using text-to-speech
        
        Args:
            text (str): Text to speak
            async_mode (bool): Run in background thread
        """
        if not text or not isinstance(text, str):
            logger.warning(f"Invalid text for speech: {text}")
            return
        
        try:
            logger.debug(f"Speaking: {text[:50]}...")
            
            if async_mode:
                # Run in background thread
                thread = threading.Thread(target=self._speak_internal, args=(text,))
                thread.daemon = True
                thread.start()
            else:
                self._speak_internal(text)
        
        except Exception as e:
            logger.error(f"Error speaking: {str(e)}")
    
    def _speak_internal(self, text):
        """Internal method to handle actual speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Error in TTS engine: {str(e)}")
    
    def stop(self):
        """Stop current speech"""
        try:
            self.engine.stop()
            logger.info("Speech stopped")
        except Exception as e:
            logger.error(f"Error stopping speech: {str(e)}")
    
    def set_rate(self, rate):
        """Set speech rate"""
        try:
            self.engine.setProperty('rate', rate)
            logger.info(f"Speech rate set to: {rate}")
        except Exception as e:
            logger.error(f"Error setting rate: {str(e)}")
    
    def set_volume(self, volume):
        """Set speech volume"""
        try:
            self.engine.setProperty('volume', volume)
            logger.info(f"Volume set to: {volume}")
        except Exception as e:
            logger.error(f"Error setting volume: {str(e)}")
