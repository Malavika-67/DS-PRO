import schedule
import time
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

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

last_state = {}


def update_database(files):

    documents = []

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

    if not documents:

        print(
            "No new documents to add."
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

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )

    db.add_documents(chunks)

    print(
        f"✅ Database updated with "
        f"{len(files)} file(s), "
        f"{len(chunks)} chunks."
    )


def check_for_changes():

    global last_state

    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    current_state = {

        f: os.path.getmtime(
            os.path.join(DATA_PATH, f)
        )

        for f in os.listdir(DATA_PATH)
    }

    changed_files = [

        f for f in current_state

        if (
            f not in last_state
            or current_state[f] != last_state[f]
        )
    ]

    if changed_files:

        print(
            f"Changes detected: "
            f"{changed_files}"
        )

        update_database(
            changed_files
        )

        last_state = current_state.copy()

    else:

        print(
            "No changes detected."
        )


schedule.every(1).minutes.do(
    check_for_changes
)

print("🔄 Updater Started")

check_for_changes()

while True:

    schedule.run_pending()

    time.sleep(1)