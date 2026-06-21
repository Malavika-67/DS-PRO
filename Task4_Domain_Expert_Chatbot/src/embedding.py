from sentence_transformers import SentenceTransformer
import numpy as np
import os


# Embedding Model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Saved Embedding File
EMBEDDING_FILE = "cs_embeddings.npy"


def create_or_load_embeddings(texts):
    """
    Create embeddings once and save them.
    Load saved embeddings on future runs.
    """

    if os.path.exists(EMBEDDING_FILE):

        print(
            "Loading saved embeddings..."
        )

        embeddings = np.load(
            EMBEDDING_FILE
        )

        return embeddings

    print(
        "Creating embeddings..."
    )

    embeddings = model.encode(
        texts,
        batch_size=256,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    np.save(
        EMBEDDING_FILE,
        embeddings
    )

    print(
        "Embeddings saved."
    )

    return embeddings


def get_query_embedding(query):
    """
    Generate embedding for user query.
    """

    embedding = model.encode(
        [query],
        convert_to_numpy=True
    )[0]

    return embedding