from openai import OpenAI


class VideoTranscriptor:
    def __init__(self):
        self.client = OpenAI()


    def transcribe(self, video_url):
        audio_file = open(video_url, 'rb')
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
        return transcription

