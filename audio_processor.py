import whisper
import sounddevice as sd
import soundfile as sf
import json
import threading

class AudioProcessor:
    def __init__(self):
        # Initialize the Whisper model in a separate thread for resource optimization
        self.model_thread = threading.Thread(target=self.init_model)
        self.model_thread.start()

    def init_model(self):
        # Load the pre-trained Whisper model
        self.model = whisper.load_model("small")

    def record_audio(self, duration=10, sample_rate=44100):
        # Record audio from the default microphone for the specified duration
        print("Recording...")
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float64')
        sd.wait()
        print("Recording finished")
        return audio, sample_rate

    def save_audio_to_file(self, audio, sample_rate, filename='recorded_audio.wav'):
        # Save the recorded audio to a file
        sf.write(filename, audio, sample_rate)

    def transcribe_audio(self, filename):
        # Wait for the model to be initialized if it's not ready
        self.model_thread.join()

        # Process the audio file and return the result
        result = self.model.transcribe(filename)
        return result

def main():
    # Instantiate the AudioProcessor class
    audio_processor = AudioProcessor()

    # Record or accept an audio file, for demonstration we'll record
    audio, sample_rate = audio_processor.record_audio()
    audio_filename = "input_audio.wav"
    audio_processor.save_audio_to_file(audio, sample_rate, audio_filename)

    # Use multithreading for resource optimization during transcription
    transcription_thread = threading.Thread(target=audio_processor.transcribe_audio, args=(audio_filename,))
    transcription_thread.start()
    transcription_thread.join()

    # Assuming transcription results are obtained here
    transcription_result = {"text": "Example transcribed text", "language": "en"}

    # Save the transcription and language detected to a JSON file
    with open("transcription_result.json", "w") as json_file:
        json.dump(transcription_result, json_file, indent=4)

    # Print the transcribed text to the console
    print("Transcribed Text:", transcription_result['text'])

if __name__ == "__main__":
    main()
