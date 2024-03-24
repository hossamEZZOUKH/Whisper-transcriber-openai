import whisper
import sounddevice as sd
import soundfile as sf
import json

def record_audio(duration=10, sample_rate=44100):
    # Record audio from the default microphone for the specified duration
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float64')
    sd.wait()
    print("Recording finished")
    return audio, sample_rate

def save_audio_to_file(audio, sample_rate, filename='recorded_audio.wav'):
    # Save the recorded audio to a file
    sf.write(filename, audio, sample_rate)

def transcribe_audio(filename):
    # Load the pre-trained Whisper model
    model = whisper.load_model("small")
    # Process the audio file and return the result
    result = model.transcribe(filename)
    return result

def main():
    # Record or accept an audio file, for demonstration we'll record
    audio, sample_rate = record_audio()
    audio_filename = "input_audio.wav"
    save_audio_to_file(audio, sample_rate, audio_filename)

    # Detect the language and transcribe the audio to text
    transcription_result = transcribe_audio(audio_filename)

    # Save the transcription and language detected to a JSON file
    with open("transcription_result.json", "w") as json_file:
        json.dump(transcription_result, json_file, indent=4)

    # Print the transcribed text to the console
    print("Transcribed Text:", transcription_result['text'])

if __name__ == "__main__":
    main()
