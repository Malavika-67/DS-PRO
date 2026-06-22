import streamlit as st
from langdetect import detect
from deep_translator import GoogleTranslator
import ollama

# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="Advanced Multilingual Chatbot",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Advanced Multilingual Chatbot")

st.write("""
This chatbot:

✅ Detects language automatically

✅ Supports multilingual conversations

✅ Maintains conversation memory

✅ Preserves context across language switches

✅ Responds in the user's language

✅ Handles ambiguous queries through clarification
""")

# -----------------------
# SESSION MEMORY
# -----------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------
# LANGUAGE MAP
# -----------------------

language_names = {
    "en": "English",
    "hi": "Hindi",
    "ta": "Tamil",
    "ml": "Malayalam",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese"
}

# -----------------------
# LANGUAGE DETECTION
# -----------------------

def detect_language(text):

    try:

        text = text.strip()

        # Avoid misclassifying short English words
        if len(text.split()) <= 2 and text.isascii():
            return "en"

        return detect(text)

    except:
        return "en"

# -----------------------
# TRANSLATION
# -----------------------

def translate_to_english(text):

    try:

        return GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

    except:
        return text


def translate_from_english(text, target_lang):

    try:

        return GoogleTranslator(
            source="en",
            target=target_lang
        ).translate(text)

    except:
        return text

# -----------------------
# CONTEXT BUILDER
# -----------------------

def build_context():

    context = ""

    # Keep last 15 exchanges

    for item in st.session_state.chat_history[-15:]:

        context += f"""
User: {item['user_en']}
Assistant: {item['assistant_en']}
"""

    return context

# -----------------------
# AMBIGUITY HANDLER
# -----------------------

def ambiguity_check(query):

    meanings = {

        "apple":
        "Apple can refer to Apple Inc., Apple products, or the fruit. Which one do you mean?",

        "python":
        "Python can refer to the programming language or the snake. Which one do you mean?",

        "java":
        "Java can refer to the programming language or the Indonesian island. Which one do you mean?",

        "jaguar":
        "Jaguar can refer to the animal or the car brand. Which one do you mean?"
    }

    return meanings.get(
        query.lower().strip()
    )

# -----------------------
# CHAT INPUT
# -----------------------

user_input = st.text_area(
    "Enter your message:"
)

if st.button("Send"):

    if user_input.strip():

        try:

            # -----------------------
            # DETECT LANGUAGE
            # -----------------------

            detected_lang = detect_language(
                user_input
            )

            # -----------------------
            # TRANSLATE TO ENGLISH
            # -----------------------

            user_en = translate_to_english(
                user_input
            )

            # -----------------------
            # AMBIGUITY CHECK
            # -----------------------

            ambiguity_response = ambiguity_check(
                user_en
            )

            if ambiguity_response:

                assistant_en = ambiguity_response

            else:

                # -----------------------
                # BUILD CONTEXT
                # -----------------------

                context = build_context()

                # -----------------------
                # PROMPT
                # -----------------------

                prompt = f"""
You are an intelligent multilingual assistant.

Rules:

1. Remember all facts shared by the user.
2. Use conversation history when answering.
3. Preserve context across language switches.
4. If asked about previous information, retrieve it from memory.
5. Maintain conversational continuity.
6. Answer only in English.
7. Be concise, accurate, and helpful.
8. Understand multilingual conversations.
9. Support cross-lingual reasoning.

Conversation History:
{context}

Current User:
{user_en}

Assistant:
"""

                # -----------------------
                # OLLAMA PHI-3
                # -----------------------

                response = ollama.chat(
                    model="phi3",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                assistant_en = response[
                    "message"
                ]["content"]

            # -----------------------
            # TRANSLATE RESPONSE
            # -----------------------

            assistant_user_lang = (
                translate_from_english(
                    assistant_en,
                    detected_lang
                )
            )

            # -----------------------
            # STORE MEMORY
            # -----------------------

            st.session_state.chat_history.append(
                {
                    "user_original": user_input,
                    "user_en": user_en,
                    "assistant_en": assistant_en,
                    "language": detected_lang
                }
            )

            # -----------------------
            # DISPLAY
            # -----------------------

            st.success(
                f"Detected Language: "
                f"{language_names.get(detected_lang, detected_lang)}"
            )

            st.markdown("### Response")

            st.write(
                assistant_user_lang
            )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )

    else:

        st.warning(
            "Please enter a message."
        )

# -----------------------
# CHAT HISTORY
# -----------------------

if st.session_state.chat_history:

    st.markdown("---")
    st.subheader(
        "Conversation History"
    )

    for item in reversed(
        st.session_state.chat_history
    ):

        st.markdown(
            f"**You:** {item['user_original']}"
        )

        st.markdown(
            f"**Bot:** {item['assistant_en']}"
        )

        st.markdown("---")