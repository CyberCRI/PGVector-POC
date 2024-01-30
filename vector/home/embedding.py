import os
from openai import OpenAI

client = OpenAI()

EMBEDDING_MODEL = "text-embedding-ada-002"

def get_embedding(text: str):
    text = text.replace("\n", " ")
    response = client.embeddings.create(input=text, model=EMBEDDING_MODEL)
    return response.data[0].embedding
