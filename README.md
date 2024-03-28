
# Whisper Audio Transcription Tool

This tool utilizes OpenAI's Whisper model to transcribe audio files to text and detect the spoken language. It supports multiple audio formats and outputs the transcription results in both JSON and text formats, stored in a dedicated results folder.

## Setup

1. **Clone the Repository**
git clone https://github.com/hossamEZZOUKH/Whisper-transcriber-openai.git
cd AI_Tools



2. **Create a Virtual Environment (Optional but Recommended)**
python3 -m venv venv
source venv/bin/activate



3. **Install Dependencies**
pip install -r requirements.txt


## Usage

1. **Run the Transcription Tool**
python audio_transcriber.py <path_to_your_audio_file>


Replace `<path_to_your_audio_file>` with the actual path to your audio file. The script will automatically convert the audio to a compatible format, transcribe it, detect the language, and save the results.

2. **View Results**
- Transcription results will be saved in the `results` folder at the same level as the script.
- JSON output: `results/transcription_result.json`
- Text output: `results/transcription_result.txt`

## Notes

- The tool currently supports a wide range of audio formats. However, the performance and accuracy of transcription may vary depending on the quality of the audio input.
- Language detection is based on the language with the most presence in the audio content and may not always match the expected language.

## Contributing

Contributions to improve the tool or extend its features are welcome. Please open an issue or submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
