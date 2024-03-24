import whisper
import json
import os
from pydub import AudioSegment

def convert_audio_format(input_filename, output_format='wav'):
    # Convert audio file to the desired format for consistent processing
    sound = AudioSegment.from_file(input_filename)
    output_filename = os.path.splitext(input_filename)[0] + '.' + output_format
    sound.export(output_filename, format=output_format)
    print(f"Converted audio saved to {output_filename}")
    return output_filename

def transcribe_audio(filename, output_filename='transcription_result.json'):
    # Load the pre-trained Whisper model
    model = whisper.load_model("small")
    # Process the audio file and return the result
    result = model.transcribe(filename)
    # Detect the language from the transcription
    detected_language = result['language']
    print(f"Detected Language: {detected_language}")
    # Save the transcription and language detected to a JSON file synchronously
    save_transcription_to_json(result, output_filename)

def save_transcription_to_json(result, filename):
    # Save the transcription result and detected language to a JSON file
    with open(filename, "w") as json_file:
        json.dump(result, json_file, indent=4)
    print(f"Transcription and language detection saved to {filename}")

def main(input_filename):
    # Convert audio to a consistent format if necessary
    converted_audio_filename = convert_audio_format(input_filename)
    # Detect the language and transcribe the audio to text synchronously
    transcribe_audio(converted_audio_filename)

if __name__ == "__main__":
    import sys
    # Accept an audio file path as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python audio_transcriber.py <audio_file_path>")
        sys.exit(1)
    main(sys.argv[1])
