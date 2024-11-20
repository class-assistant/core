from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from prompt import parse_transcription_prompt


class TranscriptionParser:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o")
        self.system_prompt = parse_transcription_prompt

    def parse_to_csv(self, headers, transcription):
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{transcription}")
        ])

        response_schemas = []
        for header in headers:
            response_schemas.append(
                ResponseSchema(
                    name=header['name'],
                    description=header['description'],
                )
            )
        parser = StructuredOutputParser.from_response_schemas(response_schemas)

        chain = prompt | self.model | parser

        return chain.invoke({
            "transcription":transcription,
            "format_instructions": parser.get_format_instructions()
        })