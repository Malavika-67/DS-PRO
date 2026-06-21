import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


def show_concept_graph(info):

    methods = info.get("Methods", [])
    datasets = info.get("Datasets", [])
    metrics = info.get("Metrics", [])

    if not methods and not datasets and not metrics:

        st.info(
            "Not enough concepts found to generate graph."
        )

        return

    G = nx.Graph()

    for method in methods:

        G.add_node(
            method,
            category="method"
        )

        for dataset in datasets:
            G.add_edge(method, dataset)

        for metric in metrics:
            G.add_edge(method, metric)

    fig, ax = plt.subplots(
        figsize=(10, 7)
    )

    pos = nx.spring_layout(
        G,
        seed=42,
        k=1
    )

    nx.draw_networkx(
        G,
        pos,
        ax=ax,
        with_labels=True,
        node_size=2500,
        font_size=9
    )

    plt.tight_layout()

    st.pyplot(fig)