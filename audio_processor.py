import whisper
import sounddevice as sd
import soundfile as sf
import json
from threading import Thread
import os
from pydub import AudioSegment

def record_audio(duration=10, sample_rate=44100, filename='recorded_audio.wav'):
    # Record audio from the default microphone for the specified duration
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float64')
    sd.wait()
    print("Recording finished")
    # Save the recorded audio to a file in a separate thread to not block the main thread
    Thread(target=save_audio_to_file, args=(audio, sample_rate, filename)).start()

def save_audio_to_file(audio, sample_rate, filename):
    # Save the recorded audio to a file
    sf.write(filename, audio, sample_rate)
    print(f"Audio saved to {filename}")

def convert_audio_format(input_filename, output_format='wav'):
    # Convert audio file to the desired format
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
    # Save the transcription and language detected to a JSON file in a separate thread
    Thread(target=save_transcription_to_json, args=(result, output_filename)).start()

def save_transcription_to_json(result, filename):
    # Save the transcription result and detected language to a JSON file
    with open(filename, "w") as json_file:
        json.dump(result, json_file, indent=4)
    print(f"Transcription and language detection saved to {filename}")

def main():
    # Record or accept an audio file; here we record
    audio_filename = "input_audio.wav"
    record_audio(filename=audio_filename)

    # Convert audio to a consistent format if necessary
    converted_audio_filename = convert_audio_format(audio_filename)

    # Detect the language and transcribe the audio to text in a separate thread
    Thread(target=transcribe_audio, args=(converted_audio_filename,)).start()

if __name__ == "__main__":
    main()
