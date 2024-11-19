import networkx as nx
import matplotlib.pyplot as plt
from langchain_community.graphs.graph_document import Node, Relationship

# Example input data (replace these with actual `Node` and `Relationship` instances from Langchain)
nodes = [
    Node(id="1", type="Person", value="Alice"),
    Node(id="2", type="Person", value="Bob"),
    Node(id="3", type="Company", value="OpenAI")
]

relationships = [
    Relationship(start_node="1", relation="works_for", end_node="3"),
    Relationship(start_node="2", relation="knows", end_node="1")
]

# Convert nodes and relationships to a NetworkX graph
G = nx.DiGraph()

# Add nodes to the graph
for node in nodes:
    G.add_node(node.id, label=node.value, type=node.type)

# Add relationships to the graph
for rel in relationships:
    G.add_edge(rel.start_node, rel.end_node, label=rel.relation)

# Plot the graph
pos = nx.spring_layout(G)  # Generate positions for nodes

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(
    G,
    pos,
    with_labels=True,
    labels=nx.get_node_attributes(G, "label"),
    node_size=2000,
    font_size=10,
    font_color="white",
    node_color="blue",
    arrowsize=20
)
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=nx.get_edge_attributes(G, "label"),
    font_size=10
)

plt.title("Graph Visualization")
plt.show()
