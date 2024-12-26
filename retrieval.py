from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_faiss_index(texts):
    embeddings = model.encode(texts)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype('float32'))
    return index, texts

def retrieve_relevant_text(query, index, texts, k=5):
    query_vector = model.encode([query])
    D, I = index.search(query_vector.astype('float32'), k)
    return [texts[i] for i in I[0]]
