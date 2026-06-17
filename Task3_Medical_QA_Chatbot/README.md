#  Medical Information Assistant

An AI-powered Medical Question Answering (QA) chatbot developed using the **MedQuAD dataset**, **Sentence Transformers**, and **Streamlit**. The application enables users to search for medical information by entering symptoms, diseases, diagnoses, or treatment-related questions and retrieves the most relevant answer using semantic similarity techniques.

---

##  Project Description

The Medical Information Assistant is designed to provide quick access to healthcare-related information from the MedQuAD dataset. Unlike traditional keyword-based search systems, this chatbot uses Natural Language Processing (NLP) and transformer-based sentence embeddings to understand the meaning behind user queries and return contextually relevant answers.

The system analyzes user input, identifies the type of medical query, computes semantic similarity with stored medical questions, and returns the best-matching answer along with a confidence score.

---

##  Key Features

- AI-powered Medical Question Answering
- Semantic Search using Sentence Transformers
- Medical Entity Detection
  - Disease
  - Symptom
  - Treatment
  - Diagnosis
  - General Medical Query
- Confidence Score Calculation
- Best Match Retrieval
- Interactive Web Interface using Streamlit
- Fast and Efficient Information Retrieval

---

##  Technologies Used

| Technology | Purpose |
|------------|----------|
| Python     | Backend Development |
| Streamlit  | User Interface |
| Sentence Transformers | Semantic Embedding Generation |
| MedQuAD Dataset | Medical Knowledge Base |
| XML ElementTree | Dataset Parsing |

---

##  Project Structure

Task3_Medical_QA_Chatbot/
│
├── .gitignore
├── app.py
├── chatbot.py
├── README.md
├── requirements.txt
│
└── MedQuAD-master/
    ├── Allergy/
    ├── Cancer/
    ├── Diabetes/
    └── ...

##  Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Task3_Medical_QA_Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

```text
http://localhost:8501
```

---

##  Working Process

1. Load the MedQuAD dataset from XML files.
2. Extract medical questions and answers.
3. Generate embeddings for all questions using the Sentence Transformer model.
4. Accept user input through the Streamlit interface.
5. Convert the user query into an embedding.
6. Compute cosine similarity between the query and dataset questions.
7. Retrieve the most relevant answer.
8. Display:
   - Detected Entity
   - Confidence Score
   - Best Matching Question
   - Corresponding Answer

---

##  Dataset Information

This project utilizes the **MedQuAD (Medical Question Answering Dataset)**, a collection of healthcare-related question-answer pairs gathered from trusted medical sources.

The dataset contains information on:

- Diseases
- Symptoms
- Treatments
- Diagnoses
- Medical Conditions
- Healthcare Procedures

---

##  Sample Query

**User Input**

```text
What are the symptoms of diabetes?
```

**System Output**

```text
Detected Entity: Symptom

Confidence Score: 0.87

Best Match:
What are the symptoms of diabetes?

Answer:
Common symptoms include increased thirst, frequent urination,
fatigue, blurred vision, and unexplained weight loss.
```

---

## Future Enhancements

- Named Entity Recognition (NER)
- Medical Intent Classification
- Multi-turn Conversational Support
- Retrieval-Augmented Generation (RAG)
- Voice-based Interaction
- Multi-language Support
- Enhanced Medical Knowledge Integration

---

##  Disclaimer

This application is intended solely for educational and research purposes.

The information provided by this chatbot should not be considered professional medical advice, diagnosis, or treatment. Users should consult qualified healthcare professionals for medical guidance and healthcare decisions.

---

##  Author

Malavika
