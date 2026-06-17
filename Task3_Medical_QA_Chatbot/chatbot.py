import os
import pickle
import warnings
import xml.etree.ElementTree as ET
from sentence_transformers import SentenceTransformer, util

warnings.filterwarnings("ignore")

base_dir = os.path.dirname(__file__)
dataset_dir = os.path.join(base_dir, "MedQuAD-master")

if not os.path.exists(dataset_dir):
    raise FileNotFoundError(
        f"Dataset folder not found: {dataset_dir}"
    )

print("Loading AI model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

questions = []
answers = []

print("Reading dataset...")

for root_dir, _, files in os.walk(dataset_dir):

    for filename in files:

        if filename.endswith(".xml"):

            file_path = os.path.join(
                root_dir,
                filename
            )

            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                for qa in root.findall(".//QAPair"):

                    q = qa.find("Question")
                    a = qa.find("Answer")

                    if (
                        q is not None and q.text and
                        a is not None and a.text and
                        a.text.strip().lower() != "none"
                    ):

                        questions.append(
                            q.text.strip()
                        )

                        answers.append(
                            a.text.strip()
                        )

            except Exception:
                pass

print(f"Loaded {len(questions)} valid questions.")

embedding_file = os.path.join(
    base_dir,
    "embeddings.pkl"
)

if os.path.exists(embedding_file):

    print("Loading saved embeddings...")

    with open(embedding_file, "rb") as f:
        question_embeddings = pickle.load(f)

else:

    print("Creating AI embeddings...")

    question_embeddings = model.encode(
        questions,
        convert_to_tensor=True,
        show_progress_bar=True
    )

    with open(embedding_file, "wb") as f:
        pickle.dump(question_embeddings, f)

print("AI ready!")


def detect_entity(question):

    q = question.lower()

    symptom_words = [
        "symptom",
        "sign",
        "pain",
        "fever"
    ]

    treatment_words = [
        "treatment",
        "treat",
        "medicine",
        "drug",
        "therapy"
    ]

    diagnosis_words = [
        "diagnosis",
        "diagnose",
        "test",
        "screening"
    ]

    if any(word in q for word in symptom_words):
        return "Symptom"

    if any(word in q for word in treatment_words):
        return "Treatment"

    if any(word in q for word in diagnosis_words):
        return "Diagnosis"

    return "Medical Query"


def get_response(user_question):

    entity = detect_entity(user_question)

    query_embedding = model.encode(
        user_question,
        convert_to_tensor=True
    )

    scores = util.cos_sim(
        query_embedding,
        question_embeddings
    )[0]

    top_result = scores.argmax().item()

    confidence = float(scores[top_result])

    if confidence < 0.60:

        return (
            f"Detected Entity: {entity}\n\n"
            f"Confidence Score: {confidence:.2f}\n\n"
            "No reliable answer found.\n"
            "Please ask a more specific medical question."
        )

    return (
        f"Detected Entity: {entity}\n\n"
        f"Confidence Score: {confidence:.2f}\n\n"
        f"Best Match:\n{questions[top_result]}\n\n"
        f"Answer:\n{answers[top_result]}"
    )