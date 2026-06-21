from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st


def show_wordcloud(texts):

    if not texts:
        st.info("No text available.")
        return

    text = " ".join(texts)

    if len(text.strip()) < 10:
        st.info("Not enough content.")
        return

    wc = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        collocations=False,
        max_words=100
    ).generate(text)

    fig, ax = plt.subplots(
        figsize=(12, 6)
    )

    ax.imshow(
        wc,
        interpolation="bilinear"
    )

    ax.axis("off")

    st.pyplot(fig)