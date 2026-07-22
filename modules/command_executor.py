"""
Command executor module for Nova
Handles system commands and application control
"""

import logging
import subprocess
import os
import sys
import webbrowser
from pathlib import Path

logger = logging.getLogger(__name__)


class CommandExecutor:
    """Execute system commands and control applications"""
    
    def __init__(self, config):
        """
        Initialize command executor
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.chrome_path = config.get("chrome", {}).get("path", "chrome.exe")
        
        # Command mappings
        self.commands = {
            "open chrome": self.open_chrome,
            "open notepad": self.open_notepad,
            "open calculator": self.open_calculator,
            "open file explorer": self.open_file_explorer,
            "open settings": self.open_settings,
            "shutdown": self.shutdown_system,
            "restart": self.restart_system,
            "lock screen": self.lock_screen,
            "sleep": self.sleep_system,
            "check weather": self.check_weather,
            "tell time": self.tell_time,
            "current time": self.tell_time,
        }
        
        logger.info("CommandExecutor initialized")
    
    def try_execute(self, command_text):
        """
        Try to execute a command if recognized
        
        Args:
            command_text (str): User command text
            
        Returns:
            bool: True if command was executed
        """
        command_lower = command_text.lower()
        
        # Check for keyword matches
        for keyword, func in self.commands.items():
            if keyword in command_lower:
                try:
                    logger.info(f"Executing command: {keyword}")
                    func()
                    return True
                except Exception as e:
                    logger.error(f"Error executing {keyword}: {str(e)}")
                    return False
        
        return False
    
    def open_chrome(self):
        """Open Google Chrome"""
        try:
            if os.path.exists(self.chrome_path):
                subprocess.Popen(self.chrome_path)
            else:
                webbrowser.open("https://www.google.com")
            logger.info("Chrome opened")
        except Exception as e:
            logger.error(f"Error opening Chrome: {str(e)}")
    
    def open_notepad(self):
        """Open Notepad"""
        try:
            subprocess.Popen("notepad.exe")
            logger.info("Notepad opened")
        except Exception as e:
            logger.error(f"Error opening Notepad: {str(e)}")
    
    def open_calculator(self):
        """Open Calculator"""
        try:
            subprocess.Popen("calc.exe")
            logger.info("Calculator opened")
        except Exception as e:
            logger.error(f"Error opening Calculator: {str(e)}")
    
    def open_file_explorer(self):
        """Open File Explorer"""
        try:
            subprocess.Popen("explorer.exe")
            logger.info("File Explorer opened")
        except Exception as e:
            logger.error(f"Error opening File Explorer: {str(e)}")
    
    def open_settings(self):
        """Open Windows Settings"""
        try:
            subprocess.Popen("ms-settings:")
            logger.info("Settings opened")
        except Exception as e:
            logger.error(f"Error opening Settings: {str(e)}")
    
    def shutdown_system(self):
        """Shutdown the system"""
        try:
            subprocess.run(["shutdown", "/s", "/t", "30", "/c", "Shutdown initiated by Nova"], 
                          capture_output=True)
            logger.info("System shutdown initiated")
        except Exception as e:
            logger.error(f"Error shutting down: {str(e)}")
    
    def restart_system(self):
        """Restart the system"""
        try:
            subprocess.run(["shutdown", "/r", "/t", "30", "/c", "Restart initiated by Nova"],
                          capture_output=True)
            logger.info("System restart initiated")
        except Exception as e:
            logger.error(f"Error restarting: {str(e)}")
    
    def lock_screen(self):
        """Lock the screen"""
        try:
            subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"],
                          capture_output=True)
            logger.info("Screen locked")
        except Exception as e:
            logger.error(f"Error locking screen: {str(e)}")
    
    def sleep_system(self):
        """Put system to sleep"""
        try:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            logger.info("System sleep initiated")
        except Exception as e:
            logger.error(f"Error putting system to sleep: {str(e)}")
    
    def check_weather(self):
        """Open weather information"""
        try:
            webbrowser.open("https://weather.com")
            logger.info("Weather page opened")
        except Exception as e:
            logger.error(f"Error opening weather: {str(e)}")
    
    def tell_time(self):
        """Get current time"""
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        logger.info(f"Current time: {current_time}")
        return current_time
    
    def search_web(self, query):
        """Search the web for a query"""
        try:
            search_url = f"https://www.google.com/search?q={query}"
            webbrowser.open(search_url)
            logger.info(f"Searching for: {query}")
        except Exception as e:
            logger.error(f"Error searching: {str(e)}")
    
    def open_url(self, url):
        """Open a specific URL"""
        try:
            if not url.startswith("http"):
                url = "https://" + url
            webbrowser.open(url)
            logger.info(f"Opened URL: {url}")
        except Exception as e:
            logger.error(f"Error opening URL: {str(e)}")
