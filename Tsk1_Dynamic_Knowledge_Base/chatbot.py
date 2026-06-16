from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DB_PATH = "vector_db"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding
)

def get_answer(query):

    try:

        results = db.similarity_search_with_score(
            query,
            k=3
        )

        if not results:
            return {
                "answer": "No relevant information found.",
                "source": "None",
                "confidence": 0
            }

        best_doc, best_score = results[0]

        # Reject weak matches
        if best_score > 1.2:

            return {
                "answer": "No relevant information found in the knowledge base.",
                "source": "None",
                "confidence": 0
            }

        answer = best_doc.page_content

        confidence = round(
            max(0, (1 / (1 + best_score)) * 100),
            2
        )

        return {
            "answer": answer,
            "source": best_doc.metadata.get(
                "source",
                "Knowledge Base"
            ),
            "confidence": confidence
        }

    except Exception as e:

        return {
            "answer": str(e),
            "source": "System",
            "confidence": 0
        }