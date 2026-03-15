import os

from dotenv import load_dotenv
from langchain_ollama import OllamaLLM


load_dotenv()

llm = OllamaLLM(
    model="mistral",
    base_url=os.getenv("BASE_URL")
)

print(llm.invoke("say hello"))



