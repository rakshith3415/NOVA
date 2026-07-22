# 🎙️ Nova - Local AI Voice Assistant

A powerful, privacy-focused voice assistant that runs entirely on your local machine using Ollama and local LLMs. Nova understands your commands, executes system tasks, and helps you interact with your computer through voice.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## ✨ Features

- **🎤 Voice Recognition** - Natural speech-to-text conversion using SpeechRecognition
- **🧠 Local AI Model** - Uses Ollama for running LLMs locally (Qwen, Llama, etc.)
- **🔊 Text-to-Speech** - Natural voice responses using pyttsx3
- **⚡ Wake Word Detection** - Activate with "Hey Nova" command
- **🖥️ System Control** - Open apps, control settings, manage system operations
- **🌐 Browser Automation** - Selenium integration for web tasks
- **🎫 Smart Booking** - Integration with flight, hotel, and ticket booking services
- **📝 Conversation Memory** - Maintains context across interactions
- **🔒 Privacy First** - Everything runs locally, no cloud dependencies
- **⚙️ Highly Configurable** - Customize models, wake words, and behaviors

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Windows/Linux/macOS
- Microphone for voice input
- [Ollama](https://ollama.ai) installed and running

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/rakshith3415/nova.git
cd nova
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. **Run setup script**
```bash
python setup.py
```

This will:
- Install all Python dependencies
- Check Ollama installation
- Download default model (optional)
- Create necessary directories

### First Run

1. **Start Ollama** (in a separate terminal)
```bash
ollama serve
```

2. **Run Nova**
```bash
# Normal mode (voice input)
python main.py

# Test mode (text input, useful for testing)
python main.py --test

# Debug mode
python main.py --debug

# Use specific model
python main.py --model qwen:7b
```

## 🎯 Usage Examples

### Voice Commands

Once running, Nova listens for the wake word "Hey Nova". After hearing it, you can say:

**System Control**
```
"Hey Nova, open Chrome"
"Hey Nova, tell me the time"
"Hey Nova, lock my screen"
"Hey Nova, open calculator"
```

**Web Browsing**
```
"Hey Nova, search for Python tutorials"
"Hey Nova, open Gmail"
"Hey Nova, check the weather"
```

**Bookings**
```
"Hey Nova, book a flight to New York"
"Hey Nova, find a hotel in Paris"
"Hey Nova, book movie tickets"
```

**System Operations**
```
"Hey Nova, shutdown the system"
"Hey Nova, put the system to sleep"
"Hey Nova, restart my computer"
```

### Test Mode

Run Nova in test mode for easier testing without voice input:

```bash
python main.py --test
```

Then type commands directly:
```
You: open notepad
Nova: Opening notepad...
```

## 📁 Project Structure

```
nova/
├── main.py                 # Entry point
├── setup.py               # Installation script
├── requirements.txt       # Python dependencies
├── config.json           # Configuration file
├── LICENSE               # MIT License
├── README.md             # This file
├── CONTRIBUTING.md       # Contribution guidelines
│
├── modules/              # Core modules
│   ├── __init__.py
│   ├── voice_input.py    # Speech recognition
│   ├── voice_output.py   # Text-to-speech
│   ├── ollama_handler.py # LLM integration
│   ├── command_executor.py # System commands
│   ├── wake_word.py      # Wake word detection
│   ├── chrome_control.py # Browser automation
│   └── booking.py        # Booking integration
│
├── utils/                # Utilities
│   ├── __init__.py
│   ├── logger.py         # Logging setup
│   └── helpers.py        # Helper functions
│
├── logs/                 # Application logs
├── data/                 # Data storage
└── cache/                # Cache directory
```

## ⚙️ Configuration

Nova is configured via `config.json`. Create it from the template or modify the default:

```json
{
  "ollama": {
    "host": "localhost",
    "port": 11434,
    "model": "qwen:7b",
    "temperature": 0.7,
    "top_p": 0.95
  },
  "voice": {
    "language": "en",
    "wake_word": "hey nova",
    "listening_timeout": 10,
    "response_timeout": 30,
    "microphone_index": 0,
    "tts_engine": "pyttsx3",
    "tts_rate": 150,
    "tts_volume": 0.9
  },
  "chrome": {
    "path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "headless": false,
    "implicit_wait": 10
  }
}
```

### Configuration Options

**Ollama Settings**
- `host`: Ollama server host
- `port`: Ollama server port
- `model`: Default LLM model
- `temperature`: Response creativity (0-1)
- `top_p`: Diversity of responses (0-1)

**Voice Settings**
- `wake_word`: Wake word to activate Nova
- `listening_timeout`: Max seconds to listen for command
- `response_timeout`: Max seconds to wait for response
- `tts_rate`: Speech rate (words per minute)
- `tts_volume`: Speech volume (0-1)

## 🔧 Supported Models

Nova works with any Ollama model. Popular choices:

| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| qwen:7b | 4.8GB | Fast | Good |
| llama2:7b | 3.8GB | Fast | Good |
| mistral:7b | 4.2GB | Fast | Excellent |
| neural-chat:7b | 4.1GB | Fast | Good |
| dolphin-mixtral:8x7b | Large | Slower | Excellent |

Download a model:
```bash
ollama pull qwen:7b
ollama pull mistral:7b
```

List downloaded models:
```bash
ollama list
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Format code
black .

# Lint code
flake8 --max-line-length=88

# Run type checking
mypy .

# Run tests
pytest
```

### Adding Custom Commands

Edit `modules/command_executor.py`:

```python
def custom_command(self):
    """My custom command"""
    try:
        # Your implementation
        logger.info("Custom command executed")
    except Exception as e:
        logger.error(f"Error: {str(e)}")

# Add to commands dictionary
self.commands["my command"] = self.custom_command
```

### Creating New Modules

1. Create file in `modules/` directory
2. Follow the template structure
3. Add logging throughout
4. Handle exceptions gracefully
5. Update `__init__.py` if needed

## 🐛 Troubleshooting

### Ollama Not Running
**Error**: `Cannot connect to Ollama at localhost:11434`

**Solution**:
```bash
# Terminal 1: Start Ollama
ollama serve

# Terminal 2: Run Nova
python main.py
```

### Microphone Not Detected
**Error**: `No microphone device found`

**Solution**:
1. Check microphone connection
2. List available microphones:
```python
import speech_recognition as sr
mic_list = sr.Microphone.list_microphone_indexes()
print(mic_list)
```
3. Update `microphone_index` in config.json

### Model Download Issues
**Error**: `Model qwen:7b not found`

**Solution**:
```bash
ollama pull qwen:7b
ollama serve  # Wait for model to download completely
```

### Speech Recognition Failing
**Solution**:
- Check microphone volume
- Reduce background noise
- Increase `listening_timeout` in config
- Try test mode: `python main.py --test`

### Chrome Not Opening
**Solution**:
1. Verify Chrome is installed
2. Update Chrome path in config.json
3. Check file permissions

## 📚 API Reference

### VoiceInput
```python
from modules.voice_input import VoiceInput
voice = VoiceInput(config)
text = voice.listen()  # Returns recognized text
```

### OllamaHandler
```python
from modules.ollama_handler import OllamaHandler
ollama = OllamaHandler(config)
response = ollama.query("What is Python?")
```

### VoiceOutput
```python
from modules.voice_output import VoiceOutput
speaker = VoiceOutput(config)
speaker.speak("Hello World")
```

### CommandExecutor
```python
from modules.command_executor import CommandExecutor
executor = CommandExecutor(config)
executor.try_execute("open chrome")
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Reporting bugs
- Suggesting features
- Submitting pull requests
- Code style requirements
- Testing procedures

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) - Local LLM framework
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Speech recognition
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) - Text-to-speech
- [Selenium](https://selenium.dev) - Browser automation
- Community contributors and testers

## 📧 Support

- **Issues**: GitHub Issues for bug reports
- **Discussions**: GitHub Discussions for questions
- **Email**: Open an issue with your contact info

## 🚦 Roadmap

- [ ] Voice activity detection
- [ ] Offline ASR (Faster Whisper)
- [ ] Advanced NLU
- [ ] Plugin system
- [ ] Web UI dashboard
- [ ] Mobile app integration
- [ ] Multi-language support
- [ ] Advanced skill learning

## 🔮 Future Enhancements

- Custom voice profiles
- Advanced booking integrations
- Smart home automation
- Calendar integration
- Email management
- Document processing
- Advanced analytics

---

**Made with ❤️ by [Rakshith Kumar](https://github.com/rakshith3415)**

⭐ If you find this project helpful, please consider giving it a star!
