from chat import ChatBot


class ChatCLI:
    def __init__(self):
        self.chatBot = ChatBot()

    def start(self):
        print("Hola, soy tu asistente virtual. Hazme una pregunta.")
        while True:
            message = input('> ')
            response = self.chatBot.chat(message)
            print(response)