from dotenv import load_dotenv
from cli import ChatCLI

load_dotenv()

if __name__ == '__main__':
    cli = ChatCLI()

    cli.start()