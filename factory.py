import csv

from chat import ChatBot
from parser import TranscriptionParser
from prompt import class_assistant_prompt
from video_transcriptor import VideoTranscriptor


def get_class_assistant_with_prompt_and_csv(csv_path):
    transcriptor = VideoTranscriptor()
    transcription_parser = TranscriptionParser()
    all_rows = []  # Lista para almacenar las filas del CSV como texto

    with open(csv_path, "r") as file, open("data/output_file.csv", "w", newline="") as output_file:
        reader = csv.reader(file, delimiter=";")
        writer = csv.writer(output_file, delimiter=";")

        headers = next(reader)
        headers.append("Objetivos")
        writer.writerow(headers)
        all_rows.append(";".join(headers))  # Agregar encabezados a la lista

        for row in reader:
            video = row[-1]  # Asumiendo que la última columna es el video
            video_transcription = transcriptor.transcribe(video)
            transcription_summary = get_summary_from_transcription(video_transcription, transcription_parser)
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
    parsed_transcription = transcription_parser.parse_to_csv(
        [
            {
                "name": "Objetivos",
                "description": "Objetivos del alumno en el curso"
            }
        ], video_transcription)

    return parsed_transcription['Objetivos']
