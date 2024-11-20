from langchain_core.messages import BaseMessage, SystemMessage
from langchain_openai import ChatOpenAI


class ChatBot:

    def __init__(self, system_prompt):
        self.model = ChatOpenAI(model="gpt-4o")
        self.systemPrompt = system_prompt
        self.history = [SystemMessage(system_prompt)]

    def chat(self, message):
        self.history.append(message)

        response = self.model.invoke(self.history)

        self.history.append(response)

        return response.content
