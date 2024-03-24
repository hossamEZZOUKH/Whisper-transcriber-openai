import unittest
import audio_processor
import os

class TestAudioProcessor(unittest.TestCase):
    def test_record_and_save_audio(self):
        # Test if recording and saving audio works
        audio_processor.record_audio(duration=3, filename="test_audio.wav")
        # Check if the audio file was created
        self.assertTrue(os.path.exists("test_audio.wav"))

    def test_transcription(self):
        # Test if transcription works; using a predefined audio file for consistency
        audio_processor.transcribe_audio("sample_audio.wav", "test_transcription.json")
        # Check if the transcription JSON file was created
        self.assertTrue(os.path.exists("test_transcription.json"))

if __name__ == "__main__":
    unittest.main()
