from langchain_openai import ChatOpenAI


class ChatBot:

    def __init__(self):
        self.history = []
        self.model = ChatOpenAI(model="gpt-4o")

    def chat(self, message):
        self.history.append(message)

        response = self.model.invoke(self.history)

        self.history.append(response)

        return response.content
