import os

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

DATA_PATH = "documents"
DB_PATH = "vector_db"

# Embedding Model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_documents():

    documents = []

    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    files = os.listdir(DATA_PATH)

    for file in files:

        path = os.path.join(DATA_PATH, file)

        try:

            if file.endswith(".txt"):

                loader = TextLoader(
                    path,
                    encoding="utf-8"
                )

                documents.extend(
                    loader.load()
                )

            elif file.endswith(".pdf"):

                loader = PyPDFLoader(path)

                documents.extend(
                    loader.load()
                )

        except Exception as e:

            print(
                f"Error loading {file}: {e}"
            )

    return documents


def update_database():

    documents = load_documents()

    if len(documents) == 0:

        print(
            "No documents found in documents folder."
        )

        return

    splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n"],
    chunk_size=250,
    chunk_overlap=30
)
    chunks = splitter.split_documents(
        documents
    )

    print(
        f"Loaded {len(documents)} documents"
    )

    print(
        f"Created {len(chunks)} chunks"
    )

    # Create or load database
    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    # Add chunks
    db.add_documents(chunks)

    print(
        "✅ Knowledge Base Updated Successfully"
    )

    print(
        f"Database Location: {DB_PATH}"
    )


if __name__ == "__main__":

    update_database()