from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_ollama import ChatOllama

import os
#import dotenv

#dotenv.load_dotenv()

def test_chat_google_generative_ai():
    "Test the ChatGoogleGenerativeAI class."
    llm = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview")
    print("Response from Google AI:", llm.invoke("What is the capital of France?").content[0]["text"])


def test_chat_ollama():
    "Test the ChatOllama class."
    llm = ChatOllama(model = "gemma3:1b")
    print("Response from Ollama AI:", llm.invoke("What is the capital of France?"))
if __name__ == "__main__":
    test_chat_google_generative_ai()
    test_chat_ollama()
