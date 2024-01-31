from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.pgvector import PGVector
from langchain_openai import OpenAIEmbeddings
import os
"""
print(len(documents))
print(texts[0])
vector = embeddings.embed_query('Testing the embeddings model')
print(vector)
doc_vectors = embeddings.embed_documents([t.page_content for t in texts[:5]])
print(doc_vectors)
"""
loader = TextLoader('sample.txt', encoding='utf-8')
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=80)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
CONNECTION_STRING = "postgresql+psycopg2://postgres:test@localhost:5432/vector_db"
COLECTION_NAME = 'state_of_union_vectors'
db = PGVector.from_documents(embedding=embeddings, documents=texts, collection_name=COLECTION_NAME, connection_string=CONNECTION_STRING)
query = "what did the president say about Russia"
similar = db.similarity_search_with_score(query,k=2)

for doc in similar:
    print(doc)
