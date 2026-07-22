"""
Wake word detection module for Nova
Detects the wake word to activate the assistant
"""

import logging
from modules.voice_input import VoiceInput

logger = logging.getLogger(__name__)


class WakeWordDetector:
    """Detect wake word activation"""
    
    def __init__(self, config):
        """
        Initialize wake word detector
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.voice_config = config.get("voice", {})
        self.wake_word = self.voice_config.get("wake_word", "hey nova").lower()
        self.voice_input = VoiceInput(config)
        
        logger.info(f"Wake word set to: {self.wake_word}")
    
    def detect(self):
        """
        Listen for wake word
        
        Returns:
            bool: True if wake word is detected
        """
        try:
            # Listen for audio
            heard_text = self.voice_input.listen()
            
            if not heard_text:
                return False
            
            heard_lower = heard_text.lower()
            logger.debug(f"Checking wake word. Heard: {heard_text}")
            
            # Check if wake word is in the heard text
            if self.wake_word in heard_lower:
                logger.info("Wake word detected!")
                return True
            
            return False
        
        except Exception as e:
            logger.error(f"Error detecting wake word: {str(e)}")
            return False
    
    def set_wake_word(self, new_wake_word):
        """
        Change the wake word
        
        Args:
            new_wake_word (str): New wake word
        """
        self.wake_word = new_wake_word.lower()
        logger.info(f"Wake word changed to: {self.wake_word}")
