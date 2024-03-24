#!/bin/bash

# This script sets up a virtual environment for running a Python script that requires the 'whisper' package

# Create a virtual environment named 'whisper_env' in the current directory
python3 -m venv whisper_env

# Activate the virtual environment
source whisper_env/bin/activate

# Install the 'whisper' package using pip
pip install openai-whisper

pip install pydub

# Deactivate the virtual environment after installation
deactivate

echo "Whisper package installed in 'whisper_env'. Use 'source whisper_env/bin/activate' to activate the environment."
