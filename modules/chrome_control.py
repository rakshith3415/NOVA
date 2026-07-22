"""
Chrome control module for Nova
Handles browser automation and web interactions
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

logger = logging.getLogger(__name__)


class ChromeControl:
    """Control Chrome browser with Selenium"""
    
    def __init__(self, config):
        """
        Initialize Chrome control
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.chrome_config = config.get("chrome", {})
        self.driver = None
        self.wait_timeout = self.chrome_config.get("implicit_wait", 10)
        
        logger.info("ChromeControl initialized")
    
    def launch_browser(self):
        """Launch Chrome browser"""
        try:
            options = webdriver.ChromeOptions()
            headless = self.chrome_config.get("headless", False)
            
            if headless:
                options.add_argument("--headless")
            
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.implicitly_wait(self.wait_timeout)
            
            logger.info("Chrome browser launched")
            return True
        
        except Exception as e:
            logger.error(f"Error launching Chrome: {str(e)}")
            return False
    
    def open_url(self, url):
        """
        Open a URL in browser
        
        Args:
            url (str): URL to open
        """
        try:
            if not self.driver:
                self.launch_browser()
            
            if not url.startswith("http"):
                url = "https://" + url
            
            self.driver.get(url)
            logger.info(f"Opened URL: {url}")
            time.sleep(2)
        
        except Exception as e:
            logger.error(f"Error opening URL: {str(e)}")
    
    def search(self, query):
        """
        Search on Google
        
        Args:
            query (str): Search query
        """
        try:
            if not self.driver:
                self.launch_browser()
            
            self.driver.get("https://www.google.com")
            search_box = self.driver.find_element(By.NAME, "q")
            search_box.send_keys(query)
            search_box.submit()
            
            logger.info(f"Searched for: {query}")
            time.sleep(2)
        
        except Exception as e:
            logger.error(f"Error searching: {str(e)}")
    
    def click_element(self, by, value):
        """
        Click an element
        
        Args:
            by: Selenium By locator type
            value: Element value
        """
        try:
            element = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            logger.info(f"Clicked element: {value}")
        
        except Exception as e:
            logger.error(f"Error clicking element: {str(e)}")
    
    def find_element(self, by, value):
        """
        Find an element
        
        Args:
            by: Selenium By locator type
            value: Element value
            
        Returns:
            WebElement or None
        """
        try:
            element = WebDriverWait(self.driver, self.wait_timeout).until(
                EC.presence_of_element_located((by, value))
            )
            logger.info(f"Found element: {value}")
            return element
        
        except Exception as e:
            logger.error(f"Error finding element: {str(e)}")
            return None
    
    def type_text(self, element, text):
        """
        Type text into an element
        
        Args:
            element: WebElement
            text: Text to type
        """
        try:
            element.clear()
            element.send_keys(text)
            logger.info(f"Typed text: {text}")
        
        except Exception as e:
            logger.error(f"Error typing text: {str(e)}")
    
    def close_browser(self):
        """Close the browser"""
        try:
            if self.driver:
                self.driver.quit()
                self.driver = None
                logger.info("Browser closed")
        
        except Exception as e:
            logger.error(f"Error closing browser: {str(e)}")
