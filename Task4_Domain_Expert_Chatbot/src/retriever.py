import numpy as np


class Retriever:

    def __init__(self, embeddings):
        self.embeddings = embeddings

        self.embeddings = (
            self.embeddings /
            np.linalg.norm(
                self.embeddings,
                axis=1,
                keepdims=True
            )
        )

    def search(
        self,
        query_embedding,
        top_k=10
    ):

        query_embedding = (
            query_embedding /
            np.linalg.norm(
                query_embedding
            )
        )

        similarities = np.dot(
            self.embeddings,
            query_embedding
        )

        top_indices = np.argsort(
            similarities
        )[::-1][:top_k]

        return top_indices