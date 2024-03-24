import whisper
import json
import os
from pydub import AudioSegment

def ensure_results_directory():
    # Ensure the results directory exists
    results_dir = os.path.join(os.path.dirname(__file__), 'results')
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    return results_dir

def convert_audio_format(input_filename, output_format='wav'):
    # Convert audio file to the desired format for consistent processing
    sound = AudioSegment.from_file(input_filename)
    output_filename = os.path.splitext(input_filename)[0] + '.' + output_format
    sound.export(output_filename, format=output_format)
    print(f"Converted audio saved to {output_filename}")
    return output_filename

def transcribe_audio(filename, results_dir):
    # Load the pre-trained Whisper model
    model = whisper.load_model("small")
    # Process the audio file and return the result
    result = model.transcribe(filename)
    # Detect the language from the transcription
    detected_language = result['language']
    print(f"Detected Language: {detected_language}")

    # Save the transcription and language detected to files in the results directory
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    save_transcription_to_files(result, base_filename, results_dir)

def save_transcription_to_files(result, base_filename, results_dir):
    # Save the transcription result and detected language to a JSON file
    json_filename = os.path.join(results_dir, f"{base_filename}_transcription.json")
    with open(json_filename, "w") as json_file:
        json.dump(result, json_file, indent=4)

    # Also save the transcription text to a .txt file
    txt_filename = os.path.join(results_dir, f"{base_filename}_transcription.txt")
    with open(txt_filename, "w") as txt_file:
        txt_file.write(result['text'])

    print(f"Transcription and language detection saved to {json_filename} and {txt_filename}")
    print(f"Full Transcription:\n{result['text']}")

def main(input_filename):
    # Ensure the results directory exists
    results_dir = ensure_results_directory()

    # Convert audio to a consistent format if necessary
    converted_audio_filename = convert_audio_format(input_filename)

    # Detect the language and transcribe the audio to text
    transcribe_audio(converted_audio_filename, results_dir)

if __name__ == "__main__":
    import sys
    # Accept an audio file path as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python audio_transcriber.py <audio_file_path>")
        sys.exit(1)
    main(sys.argv[1])
