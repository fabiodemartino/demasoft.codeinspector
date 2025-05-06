import uuid
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("code_snippets")

def vectorize_documents(documents):
    results = []
    for doc in documents:
        doc_id = str(uuid.uuid4())
        embedding = model.encode(doc["text"])
        collection.add(documents=[doc["text"]], embeddings=[embedding.tolist()], ids=[doc_id])
        results.append({"id": doc_id, "text": doc["text"]})
    return {"vectorized": results}
