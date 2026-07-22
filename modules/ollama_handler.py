"""
Ollama integration module for Nova
Handles communication with local Ollama models
"""

import logging
import requests
import json

logger = logging.getLogger(__name__)


class OllamaHandler:
    """Handle Ollama model interactions"""
    
    def __init__(self, config):
        """
        Initialize Ollama handler
        
        Args:
            config (dict): Configuration dictionary
        """
        self.config = config
        self.ollama_config = config.get("ollama", {})
        self.host = self.ollama_config.get("host", "localhost")
        self.port = self.ollama_config.get("port", 11434)
        self.model = self.ollama_config.get("model", "qwen:7b")
        self.base_url = f"http://{self.host}:{self.port}"
        
        # Test connection
        self._test_connection()
        
        logger.info(f"OllamaHandler initialized with model: {self.model}")
    
    def _test_connection(self):
        """Test connection to Ollama"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                logger.info("Successfully connected to Ollama")
            else:
                logger.warning(f"Ollama returned status {response.status_code}")
        except requests.exceptions.ConnectionError:
            logger.error(f"Cannot connect to Ollama at {self.base_url}")
            logger.error("Make sure Ollama is running: ollama serve")
        except Exception as e:
            logger.error(f"Error testing Ollama connection: {str(e)}")
    
    def query(self, prompt, conversation_history=None):
        """
        Query the Ollama model
        
        Args:
            prompt (str): User prompt
            conversation_history (list): Previous conversation messages
            
        Returns:
            str: Model response
        """
        try:
            # Build message list
            if conversation_history:
                messages = conversation_history.copy()
            else:
                messages = []
            
            # Add system message for Nova persona
            system_message = {
                "role": "system",
                "content": "You are Nova, a helpful AI assistant running locally on a Windows computer. You are helpful, concise, and friendly. When users ask you to do system tasks, acknowledge that you can help with that."
            }
            
            if not messages or messages[0].get("role") != "system":
                messages.insert(0, system_message)
            
            logger.debug(f"Querying {self.model} with prompt: {prompt[:100]}...")
            
            # Call Ollama API
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": self.ollama_config.get("stream", False),
                "temperature": self.ollama_config.get("temperature", 0.7),
                "top_p": self.ollama_config.get("top_p", 0.95),
            }
            
            response = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=self.ollama_config.get("num_predict", 128) + 60
            )
            
            if response.status_code == 200:
                result = response.json()
                
                # Extract message content
                if "message" in result:
                    content = result["message"].get("content", "")
                    logger.debug(f"Ollama response: {content[:100]}...")
                    return content.strip()
                else:
                    logger.warning(f"Unexpected response format: {result}")
                    return "I didn't get a clear response. Please try again."
            else:
                logger.error(f"Ollama API error: {response.status_code}")
                return "I'm having trouble connecting to my reasoning engine. Please try again."
        
        except requests.exceptions.ConnectionError:
            logger.error("Cannot connect to Ollama")
            return "Ollama is not running. Please start it with 'ollama serve'"
        except requests.exceptions.Timeout:
            logger.error("Ollama request timed out")
            return "The response took too long. Please try again."
        except json.JSONDecodeError:
            logger.error("Failed to parse Ollama response")
            return "I couldn't process that response. Please try again."
        except Exception as e:
            logger.error(f"Error querying Ollama: {str(e)}")
            return f"An error occurred: {str(e)}"
    
    def change_model(self, model_name):
        """
        Change the active model
        
        Args:
            model_name (str): Name of model to use (e.g., 'qwen:7b')
        """
        try:
            # Test if model exists
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": model_name, "prompt": "test", "stream": False},
                timeout=5
            )
            
            if response.status_code == 200:
                self.model = model_name
                logger.info(f"Model changed to: {model_name}")
                return True
            else:
                logger.warning(f"Model {model_name} not found")
                return False
        
        except Exception as e:
            logger.error(f"Error changing model: {str(e)}")
            return False
    
    def list_models(self):
        """
        List available models
        
        Returns:
            list: List of available models
        """
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                models = response.json().get("models", [])
                model_names = [m["name"] for m in models]
                logger.info(f"Available models: {model_names}")
                return model_names
            else:
                logger.warning(f"Failed to list models: {response.status_code}")
                return []
        
        except Exception as e:
            logger.error(f"Error listing models: {str(e)}")
            return []
