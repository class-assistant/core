import csv

from chat import ChatBot
from prompt import class_assistant_prompt
from video_transcriptor import VideoTranscriptor


def get_class_assistant_with_prompt_and_csv(csv_path):
    transcriptor = VideoTranscriptor()
    with open(csv_path, "r") as file, open("output_file.csv", "w") as output_file:

        reader = csv.reader(file, delimiter=";")
        writer = csv.writer(output_file, delimiter=";")

        headers = next(reader)
        headers.append("Objetivos")
        writer.writerow(headers)

        for row in reader:
            video = row[-1]  # I'm assuming that the last row is the video
            video_transcription = transcriptor.transcribe(video)
            transcription_summary = getSummaryFromTranscription(video_transcription)
            row.append(transcription_summary)
            writer.writerow(row)

        csv_content = "\n".join([",".join(row) for row in writer])

    final_prompt = class_assistant_prompt.replace("<<>>", csv_content)
    return ChatBot(final_prompt)


def getSummaryFromTranscription(video_transcription):
    # TODO: Add prompt where given the video transcript it returns and gets key aspects of it
    return ""
