from sentence_transformers import SentenceTransformer
import chromadb

# Initialize client
client = chromadb.Client()

# Ensure the collection exists
collection_name = "code_snippets"
try:
    collection = client.get_collection(collection_name)
except chromadb.errors.NotFoundError:
    collection = client.create_collection(collection_name)
# Initialize the sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_collection("code_snippets")

def query_vector_db(query):
    # Convert the query to an embedding
    query_embedding = model.encode(query)

    # Retrieve the most similar documents from the vector database
    results = collection.query(query_embeddings=[query_embedding.tolist()], n_results=5)

    return {"results": results["documents"]}
