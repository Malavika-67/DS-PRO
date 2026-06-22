# Task 6 - Multilingual Chatbot 
# 🌍 Advanced Multilingual Chatbot

## Overview

The Advanced Multilingual Chatbot is an AI-powered conversational assistant designed to support multilingual interactions while preserving context, intent, and conversational continuity across language switches.

The system automatically detects the user's language, translates inputs to a common processing language, maintains conversation memory, performs cross-lingual reasoning, and returns responses in the user's preferred language. It also handles ambiguous queries through clarification prompts and supports multilingual conversations using open-source AI models.

---

## Features

###  Automatic Language Detection

* Detects the user's language automatically using language identification techniques.
* Supports seamless interaction without manual language selection.

###  Multilingual Conversation Support

Supports multiple languages including:

* English
* Hindi
* Tamil
* Malayalam
* French
* Spanish
* German
* Italian
* Portuguese
* Additional languages through translation support

###  Context Retention

* Maintains conversation history across user interactions.
* Uses previous exchanges to generate context-aware responses.

###  Cross-Language Memory

* Remembers facts shared in one language.
* Retrieves and answers questions in another language.

###  Open-Source LLM Integration

* Uses locally hosted open-source language models through Ollama.
* Supports models such as Phi-3 and Gemma.

###  Ambiguity Resolution

* Detects ambiguous terms such as:

  * Apple
  * Python
  * Java
  * Jaguar
* Requests clarification before generating a response.

###  Conversational Continuity

* Preserves user intent and conversation flow across language switches.
* Ensures consistent responses regardless of the language used.

---

## System Architecture

User Input
→ Language Detection
→ Translation to English
→ Context Retrieval
→ Ambiguity Handling
→ Open-Source LLM (Ollama)
→ Response Generation
→ Translation to User Language
→ Display Response

---

## Technologies Used

### Frontend

* Streamlit

### Natural Language Processing

* LangDetect
* Deep Translator

### Large Language Model

* Ollama
* Phi-3 / Gemma

### Programming Language

* Python

---

## Project Structure


Task6_Multilingual_Chatbot/
│
├── app.py
├── requirements.txt
├── README.md


---

## Installation

### Clone the Repository

git clone <repository-url>
cd Task6_Multilingual_Chatbot


### Install Dependencies

pip install -r requirements.txt


### Install and Start Ollama

Download Ollama and install it on your system.

Start the Ollama service:


ollama serve

Pull the desired model:

ollama pull phi3


or

ollama pull gemma:2b

---

## Running the Application

Start Streamlit:


streamlit run app.py


Open the local URL displayed in the terminal.

---

## Example Test Cases

### Context Retention

User:

My favorite color is blue.


User:

मेरा पसंदीदा रंग क्या है?


Response:


Your favorite color is blue.


---

### Language Switching

User:

I live in Kerala.

User:


¿Dónde vivo?


Response:


You live in Kerala.


---

### Ambiguity Handling

User:

Apple

Response:

Apple can refer to Apple Inc., Apple products, or the fruit.
Which one do you mean?


---

## Learning Outcomes

Through this project:

* Implemented multilingual NLP workflows.
* Integrated open-source Large Language Models.
* Developed context-aware conversational AI.
* Applied language detection and translation techniques.
* Demonstrated cross-lingual reasoning capabilities.
* Built an interactive AI application using Streamlit.

---

## Future Enhancements

* Vector database integration using FAISS.
* Semantic memory retrieval.
* Voice input and speech synthesis.
* Document-based multilingual question answering.
* Advanced mixed-language sentence processing.

---

## Conclusion

This project demonstrates a context-aware multilingual chatbot capable of handling conversations across multiple languages while preserving user intent, memory, and conversational continuity. By leveraging open-source language models and NLP frameworks, the chatbot provides intelligent multilingual interactions and cross-lingual reasoning capabilities suitable for real-world conversational AI applications.

## Author

Malavika Raj B S