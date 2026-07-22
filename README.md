# Nova - Local AI Voice Assistant

A JARVIS-like voice-activated AI assistant that runs entirely on your Windows laptop using Ollama. No cloud dependencies, completely free, and fully customizable.

## Features

✅ **Voice Commands** - Speak naturally, Nova understands and responds  
✅ **Local Models** - Qwen 7B/3B, Gemma, Llama - runs 100% offline  
✅ **System Control** - Execute Windows commands, manage files, control apps  
✅ **Chrome Automation** - Open websites, search, interact with web apps  
✅ **Booking Integration** - Schedule tickets, manage calendar events  
✅ **Wake Word Detection** - "Hey Nova" activation  
✅ **Natural Voice Output** - Text-to-speech responses  
✅ **Zero Cost** - No API fees, runs on your hardware  

## Prerequisites

### Required:
- **Windows 10/11**
- **Python 3.9+**
- **Ollama** - Download from [ollama.ai](https://ollama.ai)
- **Git** (optional, for cloning)

### Recommended Hardware:
- **RAM**: 8GB minimum (16GB+ for larger models)
- **GPU**: NVIDIA/AMD (optional, for faster inference)

## Installation

### 1. Install Ollama
```bash
# Download and install from https://ollama.ai
# Verify installation
ollama --version
```

### 2. Pull Models
```bash
# Choose one or multiple models to download
ollama pull qwen:7b
ollama pull qwen:3b
ollama pull gemma:7b
ollama pull llama2:7b
ollama pull neural-chat
```

### 3. Clone Nova
```bash
git clone https://github.com/rakshith3415/nova.git
cd nova
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Nova
Edit `config.json`:
```json
{
  "model": "qwen:7b",
  "voice": "en",
  "wake_word": "hey nova",
  "listening_timeout": 10,
  "response_timeout": 30
}
```

## Usage

### Start Nova
```bash
python main.py
```

### Voice Commands Examples

| Command | Action |
|---------|--------|
| "Hey Nova, open Chrome" | Launches Google Chrome |
| "Search for weather in New York" | Opens Chrome and searches |
| "Open notepad" | Launches Notepad |
| "Tell me a joke" | AI responds with humor |
| "Run system update" | Executes Windows update |
| "Set a reminder for 5 PM" | Schedules a task |
| "Book a ticket" | Opens booking interface |
| "What time is it?" | Tells current time |
| "Shutdown in 10 minutes" | Schedules shutdown |

## Project Structure

```
nova/
├── main.py                 # Main entry point
├── config.json             # Configuration file
├── requirements.txt        # Python dependencies
├── modules/
│   ├── __init__.py
│   ├── voice_input.py      # Speech recognition
│   ├── ollama_handler.py   # Ollama integration
│   ├── voice_output.py     # Text-to-speech
│   ├── command_executor.py # System command execution
│   ├── chrome_control.py   # Browser automation
│   ├── wake_word.py        # Wake word detection
│   └── booking.py          # Booking/ticket handler
├── utils/
│   ├── logger.py           # Logging utility
│   └── helpers.py          # Helper functions
└── README.md
```

## Configuration

### Models (config.json)
```json
{
  "model": "qwen:7b",          // Model to use
  "ollama_host": "localhost",  // Ollama server
  "ollama_port": 11434,        // Ollama port
  "temperature": 0.7,          // Response creativity (0-1)
  "top_p": 0.95                // Diversity parameter
}
```

### Voice Settings
```json
{
  "voice_language": "en",      // Language code
  "tts_engine": "pyttsx3",     // Text-to-speech engine
  "wake_word": "hey nova",     // Activation phrase
  "listening_timeout": 10,     // Listen duration (seconds)
  "response_timeout": 30       // Max response time (seconds)
}
```

## Troubleshooting

### Ollama not connecting
```bash
# Check if Ollama is running
ollama list

# Restart Ollama service
ollama serve
```

### Microphone not detected
```bash
# Check audio devices
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_indexes())"
```

### Model too slow
- Switch to smaller model: `qwen:3b` or `gemma:2b`
- Enable GPU acceleration in Ollama
- Increase RAM allocation

### Wake word not triggering
- Speak clearly and at normal volume
- Check microphone input levels
- Adjust sensitivity in `config.json`

## Advanced Features

### Custom Commands
Edit `modules/command_executor.py` to add custom commands:
```python
def custom_command(query):
    if "custom action" in query.lower():
        # Your custom logic here
        return "Action completed"
```

### Integration with APIs
Add API calls in `modules/booking.py` for:
- Flight/hotel bookings
- Calendar sync
- Email notifications
- Weather APIs

### Model Switching
Switch models on-the-fly:
```bash
ollama pull qwen:3b
# Update config.json to use new model
```

## Performance Tips

1. **Use smaller models for faster response**: `qwen:3b` or `gemma:2b`
2. **Enable GPU**: Configure Ollama to use GPU acceleration
3. **Reduce context window**: Limit conversation history
4. **Run Ollama on separate process**: Better stability

## Security & Privacy

🔐 **100% Local Processing** - No data sent to cloud  
🔐 **No Account Required** - Complete offline operation  
🔐 **Open Source** - Full transparency  
🔐 **Your Data** - Complete control over all information  

## Contributing

Found a bug or have a feature request? Open an issue or submit a PR!

## License

MIT License - Feel free to use, modify, and distribute.

## Support

- 📖 Read the [Wiki](https://github.com/rakshith3415/nova/wiki)
- 🐛 Report bugs in [Issues](https://github.com/rakshith3415/nova/issues)
- 💬 Discuss features in [Discussions](https://github.com/rakshith3415/nova/discussions)

---

**Built with ❤️ for offline AI assistance**
