from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):

    text = text[:2000]

    result = summarizer(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )

    return result[0]["summary_text"]