# Task 5 - Sentiment Analysis Chatbot

##  Overview
This project implements a **Sentiment Analysis Chatbot** that interacts with users, analyzes the sentiment of their input, and provides feedback on customer satisfaction.  
It uses **Streamlit** for the user interface, **NLTK** for text preprocessing, and **Transformers (PyTorch)** for sentiment classification.


##  Project Structure
- `app.py` → Streamlit chatbot application with sentiment detection.
- `acc.py` → Accuracy evaluation script for testing model performance.
- `requirements.txt` → Python dependencies required to run the project.
- `README.md` → Documentation and usage instructions.

##  Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Malavika-67/DS-PRO.git
   cd DS-PRO/Task5_Sentiment_Analysis

2. Install dependencies:
   pip install -r requirements.txt

3. Download NLTK resources if not already installed:
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')

##  Usage

1. Run the chatbot
   
   streamlit run app.py
   
   This will launch the chatbot in your browser.

2. Run evaluation

   python acc.py

   This script evaluates the accuracy of the sentiment analysis model on test data.

##  Dependencies
 
   The project requires the following libraries (listed in requirements.txt):

1. streamlit

2. nltk

3. transformers

4. torch

##  Example

User input: "I love this product, it works perfectly!"

Chatbot response: Positive sentiment detected 

