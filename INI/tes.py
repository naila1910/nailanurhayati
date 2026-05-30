import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.title("Test Graph")

G = nx.Graph()

G.add_edge("A", "B", weight=5)
G.add_edge("B", "C", weight=3)

fig, ax = plt.subplots()

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=3000,
    ax=ax
)

labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels,
    ax=ax
)

st.pyplot(fig)