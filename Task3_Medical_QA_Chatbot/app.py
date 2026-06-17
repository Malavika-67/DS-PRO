import streamlit as st
import chatbot

st.set_page_config(
    page_title="Medical Information Assistant",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 Medical Information Assistant")

st.success(
    "Medical Question Answering Chatbot using the MedQuAD Dataset"
)

st.warning(
    "This chatbot provides information from the MedQuAD dataset. "
    "It is intended for educational purposes only and should not "
    "replace professional medical advice."
)


if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input(
    "Enter a disease, symptom, diagnosis, or treatment-related query:"
)

if st.button("Search"):

    if user_input.strip():

        with st.spinner(
            "Searching medical knowledge base..."
        ):

            response = chatbot.get_response(
                user_input
            )

        st.session_state.history.append(
            {
                "question": user_input,
                "answer": response
            }
        )

        st.subheader("Medical Information")
        st.text_area(
            "",
            response,
            height=250
        )

if st.session_state.history:

    st.subheader("Chat History")

    for item in reversed(st.session_state.history):

        with st.expander(
            f"Question: {item['question']}"
        ):
            st.text(item["answer"])