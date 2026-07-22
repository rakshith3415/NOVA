"""
Helper utilities for Nova
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

CONFIG_FILE = Path(__file__).parent.parent / "config.json"
DEFAULT_CONFIG = {
    "ollama": {
        "host": "localhost",
        "port": 11434,
        "model": "qwen:7b",
        "temperature": 0.7,
        "top_p": 0.95,
    },
    "voice": {
        "language": "en",
        "wake_word": "hey nova",
        "listening_timeout": 10,
        "response_timeout": 30,
        "microphone_index": 0,
        "tts_engine": "pyttsx3",
        "tts_rate": 150,
        "tts_volume": 0.9,
    },
    "chrome": {
        "path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "headless": False,
        "implicit_wait": 10,
    }
}


def load_config():
    """
    Load configuration from file
    
    Returns:
        dict: Configuration dictionary
    """
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                logger.info("Configuration loaded from file")
                return config
        else:
            logger.warning("Config file not found, using defaults")
            return DEFAULT_CONFIG
    except Exception as e:
        logger.error(f"Error loading config: {str(e)}")
        return DEFAULT_CONFIG


def save_config(config):
    """
    Save configuration to file
    
    Args:
        config (dict): Configuration to save
    """
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        logger.info("Configuration saved")
    except Exception as e:
        logger.error(f"Error saving config: {str(e)}")


def merge_configs(base_config, override_config):
    """
    Merge two configuration dictionaries
    
    Args:
        base_config (dict): Base configuration
        override_config (dict): Configuration to override with
        
    Returns:
        dict: Merged configuration
    """
    merged = base_config.copy()
    
    for key, value in override_config.items():
        if isinstance(value, dict) and key in merged and isinstance(merged[key], dict):
            merged[key].update(value)
        else:
            merged[key] = value
    
    return merged


def validate_config(config):
    """
    Validate configuration
    
    Args:
        config (dict): Configuration to validate
        
    Returns:
        bool: True if valid
    """
    required_keys = ["ollama", "voice", "chrome"]
    
    for key in required_keys:
        if key not in config:
            logger.warning(f"Missing required config key: {key}")
            return False
    
    logger.info("Configuration validated")
    return True


def format_duration(seconds):
    """
    Format duration in seconds to readable format
    
    Args:
        seconds (int): Duration in seconds
        
    Returns:
        str: Formatted duration
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"


def extract_time_from_text(text):
    """
    Extract time information from text
    
    Args:
        text (str): Input text
        
    Returns:
        str: Extracted time or None
    """
    import re
    
    # Pattern for time like "5 PM" or "5:30 PM"
    time_pattern = r'\d{1,2}(?::\d{2})?\s*(?:AM|PM|am|pm)'
    match = re.search(time_pattern, text)
    
    if match:
        return match.group()
    
    return None


def extract_location_from_text(text):
    """
    Extract location information from text
    
    Args:
        text (str): Input text
        
    Returns:
        str: Extracted location or None
    """
    # Common city names (basic implementation)
    cities = [
        "new york", "los angeles", "chicago", "houston", "phoenix",
        "philadelphia", "san antonio", "san diego", "dallas", "san jose",
        "london", "paris", "tokyo", "sydney", "dubai", "toronto"
    ]
    
    text_lower = text.lower()
    
    for city in cities:
        if city in text_lower:
            return city
    
    return None
