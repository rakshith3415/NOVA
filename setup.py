"""
Installation and setup script for Nova
Run this to automatically install all dependencies
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_ollama():
    """Check if Ollama is installed"""
    print("\n🤖 Checking Ollama installation...")
    try:
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Ollama found: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        pass
    
    print("⚠️  Ollama not found. Please install from https://ollama.ai")
    return False

def download_model(model="qwen:7b"):
    """Download a model for Ollama"""
    print(f"\n📥 Downloading {model}...")
    try:
        subprocess.run(["ollama", "pull", model], check=True)
        print(f"✅ Model {model} downloaded successfully!")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Error downloading model {model}")
        return False
    except FileNotFoundError:
        print("⚠️  Ollama not found. Please install Ollama first.")
        return False

def create_directories():
    """Create necessary directories"""
    print("\n📁 Creating directories...")
    dirs = ["logs", "data", "cache"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✅ Created {dir_name}/")

def main():
    """Main setup function"""
    print("=" * 50)
    print("🎙️  Nova - Local AI Voice Assistant Setup")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check Ollama
    if not check_ollama():
        print("\n⚠️  Please install Ollama from https://ollama.ai")
        response = input("Do you want to continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    else:
        # Try to download default model
        response = input("\n📥 Download default model (qwen:7b)? (y/n): ")
        if response.lower() == 'y':
            download_model("qwen:7b")
    
    print("\n" + "=" * 50)
    print("✅ Setup complete!")
    print("=" * 50)
    print("\n📖 Next steps:")
    print("1. Start Ollama: ollama serve")
    print("2. Run Nova: python main.py")
    print("3. Or use test mode: python main.py --test")
    print("\n💡 For more info, see README.md")

if __name__ == "__main__":
    main()
