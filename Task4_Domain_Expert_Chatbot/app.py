import streamlit as st

from src.data_loader import load_data

from src.embedding import (
    create_or_load_embeddings,
    get_query_embedding
)

from src.retriever import Retriever

from src.llm_explainer import (
    generate_answer,
    summarize_text
)

from src.extractor import (
    extract_research_info
)

from src.visualization import (
    show_wordcloud
)

from src.concept_graph import (
    show_concept_graph
)


st.set_page_config(
    page_title="ArXiv Expert Chatbot",
    layout="wide"
)

st.title("📚 ArXiv Expert Chatbot")

st.write("""
Research Paper Search, Summarization,
Concept Explanation, Information Extraction,
and Visualization.
""")


# -----------------------------
# Session Memory
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []


# -----------------------------
# Load Dataset + Embeddings
# -----------------------------
@st.cache_data
def initialize():

    df = load_data(
        limit=30000,
        category_filter="cs"
    )

    texts = (
        df["title"] +
        " " +
        df["summary"]
    ).tolist()

    embeddings = create_or_load_embeddings(
        texts
    )

    retriever = Retriever(
        embeddings
    )

    return df, retriever


with st.spinner(
    "Loading Computer Science papers..."
):

    df, retriever = initialize()


st.success(
    f"Loaded {len(df)} Computer Science papers from arXiv."
)


# -----------------------------
# Search Mode
# -----------------------------
search_mode = st.selectbox(
    "Search Mode",
    [
        "Semantic Search",
        "Title Search"
    ]
)


query = st.text_input(
    "Enter Research Question"
)


# -----------------------------
# Main Search Logic
# -----------------------------
if query:

    if search_mode == "Title Search":

        papers = df[
            df["title"]
            .str.lower()
            .str.contains(
                query.lower(),
                na=False
            )
        ]

        if len(papers) == 0:

            st.warning(
                "No matching papers found."
            )

            st.stop()

        papers = papers.head(5)

        context = "\n\n".join(
            papers["summary"].tolist()
        )

    else:

        query_embedding = (
            get_query_embedding(query)
        )

        indices = retriever.search(
            query_embedding,
            top_k=8
        )

        papers = df.iloc[
            indices
        ]

        context = "\n\n".join(
            papers["summary"].tolist()
        )

    # -----------------------------
    # Conversation History Context
    # -----------------------------
    history_text = "\n".join([
        f"User: {q}\nAssistant: {a}"
        for q, a in st.session_state.history[-5:]
    ])

    # -----------------------------
    # Generate Expert Answer
    # -----------------------------
    with st.spinner(
        "Generating expert answer..."
    ):

        answer = generate_answer(
            query,
            context,
            history_text
        )

    st.session_state.history.append(
        (
            query,
            answer
        )
    )

    # -----------------------------
    # Expert Answer
    # -----------------------------
    st.subheader(
        "🧠 Expert Answer"
    )

    st.write(answer)

    # -----------------------------
    # Top Papers
    # -----------------------------
    st.subheader(
        "📄 Top Research Papers"
    )

    paper_texts = []

    for _, row in papers.iterrows():

        title = row["title"]
        summary = row["summary"]

        paper_texts.append(
            summary
        )

        st.markdown(
            f"### {title}"
        )

        st.write(
            "**Original Abstract:**"
        )

        st.write(summary)

        with st.spinner(
            "Generating summary..."
        ):

            paper_summary = summarize_text(
                summary
            )

        st.write(
            "**Paper Summary:**"
        )

        st.write(
            paper_summary
        )

        st.markdown("---")

    # -----------------------------
    # Information Extraction
    # -----------------------------
    st.subheader(
        "🔍 Extracted Research Information"
    )

    info = extract_research_info(
        context
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.write("### Methods")

        if info["Methods"]:

            for item in info["Methods"]:
                st.success(item)

        else:
            st.write("No methods found")

    with col2:

        st.write("### Datasets")

        if info["Datasets"]:

            for item in info["Datasets"]:
                st.info(item)

        else:
            st.write("No datasets found")

    with col3:

        st.write("### Metrics")

        if info["Metrics"]:

            for item in info["Metrics"]:
                st.warning(item)

        else:
            st.write("No metrics found")

    # -----------------------------
    # WordCloud
    # -----------------------------
    st.subheader(
        "☁️ Concept WordCloud"
    )

    show_wordcloud(
        paper_texts
    )

    # -----------------------------
    # Concept Graph
    # -----------------------------
    st.subheader(
        "🕸️ Concept Graph"
    )

    show_concept_graph(
        info
    )


# -----------------------------
# Sidebar History
# -----------------------------
if len(st.session_state.history) > 0:

    st.sidebar.title(
        "Conversation History"
    )

    for i, (q, _) in enumerate(
        reversed(
            st.session_state.history
        )
    ):

        st.sidebar.write(
            f"{i+1}. {q}"
        )