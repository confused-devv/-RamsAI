import faiss
import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")  # lightweight

# Create/load FAISS index
dimension = 384
index_file = "recipe_index.faiss"

if os.path.exists(index_file):
    index = faiss.read_index(index_file)
    with open("recipe_texts.txt", "r", encoding="utf-8") as f:
        known_texts = f.read().splitlines()
else:
    index = faiss.IndexFlatL2(dimension)
    known_texts = []

def is_novel(text, threshold=0.7):
    if not known_texts:
        return True  # nothing to compare to

    vector = model.encode([text])
    D, _ = index.search(vector, k=1)
    return D[0][0] > (1 - threshold)

def add_to_index(text):
    vector = model.encode([text])
    index.add(vector)
    known_texts.append(text)

    faiss.write_index(index, index_file)
    with open("recipe_texts.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(known_texts))
