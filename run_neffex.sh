#!/bin/bash

echo "🚀 Starting Neffex AI Installation and Launch Script..."

# 1. Update & Install system dependencies
echo "📦 Installing system dependencies..."
sudo apt update && sudo apt install -y python3 python3-pip python3-venv build-essential portaudio19-dev libasound2-dev libffi-dev libnss3-tools espeak

# 2. Set up Python Virtual Environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 3. Install Python packages
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install speechrecognition pyttsx3 pyaudio flask openai requests googletrans==4.0.0-rc1

# Optional: Install extra packages if you're using Edge TTS, Bark, etc.
# pip install edge-tts bark voicefixer ...

# 4. Display directory structure
echo "📁 Folder structure:"
if command -v tree >/dev/null 2>&1; then
    tree .
else
    echo "(Tree command not found. Showing with ls -R)"
    ls -R
fi

# 5. Launch main Neffex AI core system
echo "🚀 Running Neffex AI core system..."
python3 core/brain.py &

# 6. Launch web panel in new terminal (if gnome-terminal is available)
if command -v gnome-terminal >/dev/null 2>&1; then
    gnome-terminal -- bash -c "source venv/bin/activate && python3 web_panel/app.py; exec bash"
else
    echo "🖥️ 'gnome-terminal' not found. Launching web panel in this terminal..."
    python3 web_panel/app.py
fi
