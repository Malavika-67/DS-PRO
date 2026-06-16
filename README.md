
# Dynamic Knowledge Base Chatbot

## Project Overview

The Dynamic Knowledge Base Chatbot is an AI-powered document retrieval system that automatically expands its knowledge base whenever new documents are added. The project utilizes Chroma Vector Database and Hugging Face Sentence Transformers to perform semantic search over uploaded TXT and PDF documents.

The chatbot continuously updates its vector database and retrieves relevant information based on user queries, fulfilling the objective of dynamic knowledge base expansion.

---

## Objective

To implement a chatbot capable of dynamically updating its knowledge base by periodically incorporating new information from specified document sources and retrieving relevant responses using vector similarity search.

---

## Key Features

* Dynamic Knowledge Base Expansion
* Automatic Document Ingestion
* TXT and PDF File Support
* Semantic Search using Vector Embeddings
* Chroma Vector Database Integration
* Confidence Score Calculation
* Source Document Tracking
* Streamlit-Based User Interface
* Periodic Knowledge Base Updates
* Low-Latency Information Retrieval

---

## Technologies Used

| Technology              | Purpose                      |
| ----------------------- | ---------------------------- |
| Python                  | Core Programming Language    |
| Streamlit               | User Interface               |
| LangChain               | Document Processing Pipeline |
| ChromaDB                | Vector Database              |
| Hugging Face Embeddings | Text Embedding Generation    |
| Sentence Transformers   | Semantic Search              |
| PyPDF                   | PDF Document Loading         |
| Schedule                | Automated Updates            |

---

## Project Structure

Dynamic-Knowledge-Base-Chatbot/

├── app.py

├── chatbot.py

├── ingest.py

├── updater.py

├── requirements.txt

├── README.md

├── .gitignore

├── documents/

│ ├── ai.txt

│ └── new_articles.txt

└── vector_db/ (generated automatically)

---

## Workflow

1. Documents are stored inside the documents folder.
2. The ingestion module loads TXT and PDF files.
3. Documents are divided into chunks using recursive text splitting.
4. Embeddings are generated using Sentence Transformers.
5. Chunks are stored in Chroma Vector Database.
6. User queries are converted into embeddings.
7. Similarity search retrieves the most relevant content.
8. The chatbot returns the answer along with source information and confidence score.

---

## Installation

### Clone Repository

git clone <repository-url>

cd Dynamic-Knowledge-Base-Chatbot

### Install Dependencies

pip install -r requirements.txt

---

## Build the Knowledge Base

python ingest.py

This creates the vector database from all documents inside the documents folder.

---

## Run Automatic Updater

python updater.py

The updater continuously monitors the documents directory and updates the vector database whenever files are added or modified.

---

## Launch the Application

streamlit run app.py

---

## Sample Topics Included

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Neural Networks
* Data Science
* Generative AI
* Cloud Computing
* Edge Computing
* Cybersecurity
* Blockchain
* Internet of Things (IoT)
* Big Data
* Augmented Reality (AR)
* Virtual Reality (VR)
* Quantum Computing
* Robotics

---

## Expected Outcome

The chatbot automatically incorporates newly added information into its responses by periodically updating the vector database, enabling continuous knowledge base growth without manual retraining.

---

## Future Enhancements

* Retrieval-Augmented Generation (RAG)
* LLM Integration (Llama 3 / GPT Models)
* Multi-Document Summarization
* Web-Based Knowledge Ingestion
* Conversational Memory
* Advanced Re-ranking Techniques
* User Authentication and Access Control

---

## Author

Malavika


