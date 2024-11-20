from factory import get_class_assistant_with_prompt_and_csv


class ChatCLI:
    def __init__(self):
        self.chatBot = get_class_assistant_with_prompt_and_csv('./data/sample.csv')

    def start(self):
        print("Hola, soy tu asistente virtual.")
        message = 'Cuentame sobre la clase'
        response = self.chatBot.chat(message)
        print(response)
        while True:
            message = input('==> ')
            response = self.chatBot.chat(message)
            print(response)