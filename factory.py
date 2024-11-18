import csv

from chat import ChatBot
from prompt import class_assistant_prompt


def get_class_assistant_with_prompt_and_csv(csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        csv_content = "\n".join([",".join(row) for row in reader])

    final_prompt = class_assistant_prompt.replace('<<>>', csv_content)
    return ChatBot(final_prompt)