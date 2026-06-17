import streamlit as st
from PIL import Image
import numpy as np
import easyocr
from transformers import BlipProcessor, BlipForConditionalGeneration

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Multi-Modal AI Assistant",
    layout="wide"
)

st.title("🤖 Multi-Modal AI Assistant")
st.write(
    "Analyze images, extract text, maintain context, and provide evidence-based responses."
)

# ----------------------------------
# LOAD MODELS
# ----------------------------------

@st.cache_resource
def load_models():
    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    caption_model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    ocr_reader = easyocr.Reader(
        ["en"],
        gpu=False
    )

    return processor, caption_model, ocr_reader


processor, caption_model, ocr_reader = load_models()

# ----------------------------------
# SESSION STATE
# ----------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "image_facts" not in st.session_state:
    st.session_state.image_facts = {}

if "caption" not in st.session_state:
    st.session_state.caption = ""

if "ocr_text" not in st.session_state:
    st.session_state.ocr_text = ""

# ----------------------------------
# CLEAR CHAT
# ----------------------------------

if st.button("🗑 Clear Conversation"):
    st.session_state.chat_history = []
    st.session_state.image_facts = {}
    st.session_state.caption = ""
    st.session_state.ocr_text = ""
    st.rerun()

# ----------------------------------
# IMAGE UPLOAD
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

# ----------------------------------
# IMAGE ANALYSIS
# ----------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Analyze Image"):

        with st.spinner("Analyzing Image..."):

            # Caption Generation
            inputs = processor(
                images=image,
                return_tensors="pt"
            )

            output = caption_model.generate(
                **inputs,
                max_new_tokens=50
            )

            caption = processor.decode(
                output[0],
                skip_special_tokens=True
            )

            # OCR
            try:
                image_np = np.array(image)

                ocr_results = ocr_reader.readtext(
                    image_np,
                    detail=0
                )

                extracted_text = (
                    "\n".join(ocr_results)
                    if ocr_results
                    else "No text detected."
                )

            except Exception as e:
                extracted_text = f"OCR Error: {e}"

            # Store Facts
            st.session_state.caption = caption
            st.session_state.ocr_text = extracted_text

            st.session_state.image_facts = {
                "caption": caption,
                "ocr": extracted_text
            }

        st.success("Analysis Complete")

# ----------------------------------
# SHOW VISUAL EVIDENCE
# ----------------------------------

if st.session_state.image_facts:

    st.subheader("📷 Visual Evidence")

    st.write("**Image Caption:**")
    st.write(st.session_state.caption)

    st.write("**Detected Text:**")
    st.write(st.session_state.ocr_text)

# ----------------------------------
# REASONING FUNCTION
# ----------------------------------

def generate_reasoned_answer(question, facts, history):

    caption = facts.get("caption", "")
    ocr_text = facts.get("ocr", "")

    q = question.lower()

    evidence = []

    if caption:
        evidence.append(f"Caption Evidence: {caption}")

    if ocr_text and ocr_text != "No text detected.":
        evidence.append(f"OCR Evidence: {ocr_text}")

    if "text" in q or "written" in q or "word" in q:

        if ocr_text and ocr_text != "No text detected.":

            answer = (
                "The image contains the following text:\n\n"
                f"{ocr_text}"
            )

        else:

            answer = (
                "I could not find readable text in the image."
            )

    elif "describe" in q or "what is in the image" in q:

        answer = (
            f"The image appears to show: {caption}"
        )

    elif "why" in q or "evidence" in q:

        answer = (
            "My answer is based on visual captioning and OCR evidence extracted from the image."
        )

    elif "animal" in q or "object" in q or "person" in q:

        answer = (
            f"Based on visual analysis, I found: {caption}"
        )

    elif "dangerous" in q:

        answer = (
            "I cannot reliably determine danger from the image alone. Additional context is needed."
        )

    elif "previous" in q or "earlier" in q:

        if len(history) >= 2:

            answer = (
                f"The previous discussion was about: {history[-2][1]}"
            )

        else:

            answer = (
                "No previous conversation context is available."
            )

    else:

        answer = (
            f"Based on available evidence, the image depicts: {caption}"
        )

    return answer, evidence

# ----------------------------------
# CHAT SECTION
# ----------------------------------

if st.session_state.image_facts:

    st.subheader("💬 Ask Questions")

    user_question = st.text_input(
        "Ask a question about the image"
    )

    if user_question:

        answer, evidence = generate_reasoned_answer(
            user_question,
            st.session_state.image_facts,
            st.session_state.chat_history
        )

        st.session_state.chat_history.append(
            ("User", user_question)
        )

        st.session_state.chat_history.append(
            ("Assistant", answer)
        )

        st.subheader("✅ Answer")
        st.write(answer)

        st.subheader("📌 Supporting Evidence")

        for item in evidence:
            st.write("-", item)

# ----------------------------------
# CHAT HISTORY
# ----------------------------------

if st.session_state.chat_history:

    st.subheader("📜 Conversation History")

    for speaker, message in st.session_state.chat_history:

        if speaker == "User":
            st.markdown(f"👤 **You:** {message}")

        else:
            st.markdown(f"🤖 **Assistant:** {message}")