from deepgram import DeepgramClient, PrerecordedOptions


class VideoTranscriptor:
    def __init__(self):
        self.client = DeepgramClient()
        self.options = PrerecordedOptions(
            punctuate=True, model="nova-2", language="es-419"
        )

    def transcribe(self, video_url):
        response = self.client.listen.prerecorded.v('1').transcribe_url(video_url, self.options)
        return response['results']['channels'][0]['alternatives'][0]['transcript']
