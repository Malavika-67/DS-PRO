import streamlit as st
import os

from ingest import update_database
from chatbot import get_answer

st.set_page_config(
    page_title="Dynamic Knowledge Base Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title(
    "🤖 Dynamic Knowledge Base Chatbot"
)

st.caption(
    "Automatically learns from uploaded documents."
)

if not os.path.exists("documents"):
    os.makedirs("documents")

# Sidebar
st.sidebar.title("Knowledge Base")

files = os.listdir("documents")

st.sidebar.metric(
    "Documents",
    len(files)
)

st.sidebar.subheader(
    "Indexed Files"
)

for file in files:
    st.sidebar.write(file)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload
uploaded_file = st.file_uploader(
    "Upload TXT or PDF",
    type=["txt", "pdf"]
)

if uploaded_file:

    save_path = os.path.join(
        "documents",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(
            uploaded_file.getbuffer()
        )

    update_database()

    st.success(
        "Knowledge Base Updated!"
    )

# Chat input
query = st.chat_input(
    "Ask a question..."
)

if query:

    result = get_answer(query)

    st.session_state.messages.append(
        ("user", query)
    )

    st.session_state.messages.append(
        ("assistant", result)
    )

# Display chat
for role, message in st.session_state.messages:

    with st.chat_message(role):

        if role == "assistant":

            st.write(
                message["answer"]
            )

            st.caption(
                f"📄 Source: {message['source']}"
            )

            st.caption(
                f"🎯 Confidence: {message['confidence']}%"
            )

        else:
            st.write(message)