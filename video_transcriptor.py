from deepgram import DeepgramClient, PrerecordedOptions

class VideoTranscriptor:
    def __init__(self):
        self.client = DeepgramClient()
        self.options = PrerecordedOptions(
            punctuate=True, model="nova-2", language="es-419"
        )

    def transcribe(self, video_path):
        with open(video_path, 'rb') as buffer_data:
            payload = {'buffer': buffer_data}

        response = self.client.listen.prerecorded.v('1').transcribe_file(payload, self.options)
        return response['results']['channels'][0]['alternatives'][0]['transcript']