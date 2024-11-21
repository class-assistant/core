import csv
from parser import TranscriptionParser

from chat import ChatBot
from prompt import class_assistant_prompt
from video_transcriptor import VideoTranscriptor


def get_class_assistant_with_prompt_and_csv(csv_path):
    transcriptor = VideoTranscriptor()
    transcription_parser = TranscriptionParser()
    all_rows = []  # Lista para almacenar las filas del CSV como texto

    with open(csv_path, "r") as file, open(
        "data/output_file.csv", "w", newline=""
    ) as output_file:
        reader = csv.reader(file, delimiter=";")
        writer = csv.writer(output_file, delimiter=";")

        headers = next(reader)
        new_headers = [
            "Expectativas del curso",
            "Qué se quiere llevar de conocimiento de sus compañeros?",
            "Que le va a aportar al grupo?",
            "Cómo le gustaría que esta experiencia lo ayude a crecer?",
        ]

        headers.extend(new_headers)
        writer.writerow(headers)
        all_rows.append(";".join(headers))  # Agregar encabezados a la lista

        for row in reader:
            video = row[-1]  # Asumiendo que la última columna es el video
            video_transcription = transcriptor.transcribe(video)
            transcription_summary = get_summary_from_transcription(
                video_transcription, transcription_parser
            )
            row.append(transcription_summary)
            writer.writerow(row)
            all_rows.append(";".join(row))  # Agregar cada fila al CSV acumulado

    # Convertir la lista a una cadena con formato CSV
    csv_content = "\n".join(all_rows)

    # Escribir el contenido del CSV en un archivo separado
    with open("csv_content_output.txt", "w") as text_file:
        text_file.write(csv_content)

    # Reemplazar la plantilla
    final_prompt = class_assistant_prompt.replace("<<>>", csv_content)
    return ChatBot(final_prompt)


def get_summary_from_transcription(video_transcription, transcription_parser):

    questions = [
        {
            "name": "Expectativas del curso",
            "description": "Expectativas del alumno en el curso",
        },
        {
            "name": "Qué se quiere llevar de conocimiento de sus compañeros?",
            "description": "Conocimiento que el alumno quiere obtener de sus compañeros",
        },
        {
            "name": "Que le va a aportar al grupo?",
            "description": "Las capacidades, fortalezas y conocimientos que el alumno le va a aportar a sus compañeros",
        },
        {
            "name": "Cómo le gustaría que esta experiencia lo ayude a crecer?",
            "description": "De que manera le gustaria al alumno que el curso lo ayude a crecer de manera personal y profesional",
        },
    ]

    parsed_transcription = transcription_parser.parse_to_csv(
        questions, video_transcription
    )

    attributes = [parsed_transcription[question["name"]] for question in questions]

    return ";".join(attributes)
