# Task 4 - Domain Expert Chatbot
# 📚 ArXiv Expert Chatbot

## Overview

ArXiv Expert Chatbot is an AI-powered research assistant designed to help users explore Computer Science research papers from the arXiv repository. The system combines semantic search, research paper retrieval, summarization, question answering, information extraction, and visualization techniques to provide an interactive research experience.

The chatbot leverages Sentence Transformers for semantic retrieval, Ollama with Gemma 2B for intelligent responses, and Streamlit for the user interface.

---

## Features

### Semantic Research Search

* Retrieve relevant research papers using semantic similarity.
* Search across thousands of Computer Science papers from arXiv.

### Research Paper Summarization

* Generate concise summaries of retrieved papers.
* Highlight research objectives, methodology, key findings, and significance.

### Expert Question Answering

* Answer research-related questions using retrieved paper content.
* Maintain conversation context during the session.

### Information Extraction

Automatically extracts:

* Methods
* Datasets
* Evaluation Metrics

from retrieved research papers.

### Word Cloud Visualization

* Generate visual representations of frequently occurring research concepts.

### Concept Graph Visualization

* Visualize relationships between methods, datasets, and performance metrics.

### Session Memory

* Store recent user interactions for context-aware responses.

---

## Project Structure

ArXiv_Expert_Chatbot/

├── app.py

├── data/
│ └── arxiv-metadata-oai-snapshot.json

├── src/
│ ├── data_loader.py
│ ├── embedding.py
│ ├── retriever.py
│ ├── llm_explainer.py
│ ├── extractor.py
│ ├── visualization.py
│ └── concept_graph.py

├── cs_embeddings.npy

├── requirements.txt

└── README.md

---

## Installation

1. Clone the repository.

2. Create a virtual environment:

   python -m venv venv

3. Activate the virtual environment.

   Windows:

   venv\Scripts\activate

   Linux/macOS:

   source venv/bin/activate

4. Install dependencies:

   pip install -r requirements.txt

---

## Ollama Setup

1. Install Ollama from https://ollama.com

2. Download the Gemma model:

   ollama pull gemma:2b

3. Verify installation:

   ollama list

---

## Dataset Setup

Place the arXiv metadata dataset file inside:

data/arxiv-metadata-oai-snapshot.json

The application automatically loads Computer Science papers from the dataset.

---

## Running the Application

Start Ollama:

ollama serve

Run the Streamlit application:

streamlit run app.py

The application will launch in your browser at:

http://localhost:8501

---

## Example Queries

* What is Deep Learning?
* Explain Reinforcement Learning.
* Compare CNN and Transformer architectures.
* Explain Graph Neural Networks.
* What datasets are commonly used for image classification?
* Compare supervised and unsupervised learning.

---

## Technologies Used

* Python
* Streamlit
* Sentence Transformers
* Ollama
* Gemma 2B
* Pandas
* NumPy
* NetworkX
* Matplotlib
* WordCloud
* LangChain

---

## Outcomes

This project demonstrates:

* Semantic Search
* Research Paper Retrieval
* Automated Summarization
* Question Answering
* Information Extraction
* Data Visualization
* Retrieval-Augmented Generation (RAG)

The system serves as an intelligent research assistant for students, researchers, and AI enthusiasts.

---

## Author

Malavika Raj B S