#!/bin/bash

# This script activates the virtual environment and runs the audio_transcriber.py script

# Activate the virtual environment
source whisper_env/bin/activate

# Run the audio_transcriber.py script with any additional arguments passed to this script
python3 /Users/mac/Desktop/AI_Tools/whisper/audio_transcriber_v2.py "$@"

# Deactivate the virtual environment after running the script
deactivate
