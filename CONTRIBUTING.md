# Contributing to Nova

Thank you for your interest in contributing to Nova! We welcome contributions from everyone. This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Report issues responsibly
- Help others learn and grow

## How to Contribute

### Reporting Bugs

1. **Check existing issues** - Search to avoid duplicates
2. **Create detailed report** - Include:
   - Steps to reproduce
   - Expected vs actual behavior
   - System info (Windows version, Python version, etc.)
   - Error messages and logs
3. **Use issue template** if available

### Suggesting Features

1. **Check discussions** - See if it's already discussed
2. **Describe the feature** clearly:
   - Problem it solves
   - Use cases
   - Proposed implementation (optional)
3. **Provide examples** if possible

### Pull Requests

#### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/rakshith3415/nova.git
cd nova

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

#### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Follow coding standards**
   - Use PEP 8 style guide
   - Add docstrings to functions and classes
   - Write meaningful commit messages
   - Keep functions focused and single-purpose

3. **Write tests**
   ```bash
   pytest tests/
   ```

4. **Check code quality**
   ```bash
   # Format code
   black .
   
   # Lint code
   flake8 --max-line-length=88
   
   # Type checking
   mypy .
   ```

#### Commit Guidelines

```bash
# Good commit message
git commit -m "Add wake word detection enhancement"
git commit -m "Fix microphone initialization on Windows"

# Avoid
git commit -m "fixed stuff"
git commit -m "WIP: work in progress"
```

#### Pull Request Process

1. **Update documentation** - Add docstrings, update README if needed
2. **Test thoroughly** - Run all tests before submitting
3. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
4. **Create Pull Request** with:
   - Clear title and description
   - Reference to related issues
   - List of changes
   - Any breaking changes

5. **Respond to feedback** - Be open to suggestions

## Development Guidelines

### Code Style

```python
"""
Good example:
- Clear docstrings
- Type hints where helpful
- Meaningful variable names
"""

def process_audio(audio_input: str) -> str:
    """
    Process audio input and return text.
    
    Args:
        audio_input: Raw audio data
        
    Returns:
        Processed text output
        
    Raises:
        ValueError: If audio is invalid
    """
    if not audio_input:
        raise ValueError("Audio input cannot be empty")
    
    result = _internal_process(audio_input)
    return result
```

### File Organization

```
nova/
├── modules/          # Core functionality
│   ├── voice_input.py
│   ├── ollama_handler.py
│   └── ...
├── utils/            # Helper utilities
│   ├── logger.py
│   └── helpers.py
├── tests/            # Test files
├── main.py           # Entry point
└── config.json       # Configuration
```

### Adding New Modules

1. **Create module file** in `modules/` directory
2. **Add class-based structure** for functionality
3. **Include docstrings** for all public methods
4. **Add logging** for debugging
5. **Handle exceptions** gracefully
6. **Update imports** in `__init__.py`

Example:

```python
"""
New module template
"""

import logging

logger = logging.getLogger(__name__)

class NewFeature:
    """Brief description of the feature"""
    
    def __init__(self, config):
        """Initialize with configuration"""
        self.config = config
        logger.info("NewFeature initialized")
    
    def do_something(self):
        """Perform the main action"""
        try:
            # Implementation
            logger.info("Action completed")
        except Exception as e:
            logger.error(f"Error: {str(e)}")
```

## Testing

### Writing Tests

```python
# tests/test_voice_input.py
import pytest
from modules.voice_input import VoiceInput

class TestVoiceInput:
    """Test voice input module"""
    
    def test_initialization(self, config):
        """Test VoiceInput initialization"""
        voice_input = VoiceInput(config)
        assert voice_input is not None
    
    def test_listen_timeout(self, config):
        """Test listen timeout"""
        # Test implementation
        pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_voice_input.py

# Run with coverage
pytest --cov=modules tests/
```

## Documentation

### README Updates

- Keep README.md current with new features
- Update installation instructions if needed
- Add examples for new functionality
- Update troubleshooting section

### Code Documentation

- Write docstrings for all modules, classes, and functions
- Use Google-style docstrings:
  ```python
  def function(param):
      """Brief description.
      
      Longer description if needed.
      
      Args:
          param: Parameter description
          
      Returns:
          Return value description
          
      Raises:
          Exception: When something goes wrong
      """
  ```

## Branching Strategy

```
main                 # Stable releases
├── develop          # Development branch
│   ├── feature/*    # New features
│   ├── bugfix/*     # Bug fixes
│   └── docs/*       # Documentation
```

## Release Process

1. **Update version** in appropriate files
2. **Update CHANGELOG** with new features/fixes
3. **Create release notes** with highlights
4. **Tag release** `git tag v1.0.0`
5. **Merge to main** after review

## Areas for Contribution

### High Priority
- [ ] Better wake word detection algorithms
- [ ] Offline text-to-speech options
- [ ] Performance optimizations
- [ ] Error handling improvements

### Medium Priority
- [ ] Additional command templates
- [ ] More Ollama model support
- [ ] Web UI for configuration
- [ ] Advanced logging features

### Low Priority
- [ ] Additional language support
- [ ] More booking integrations
- [ ] Enhanced documentation
- [ ] Example plugins

## Getting Help

- **Documentation**: Check README.md and inline code comments
- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Search existing issues for similar problems
- **Chat**: Join our community discussions

## License

By contributing to Nova, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for helping make Nova better! 🚀
