import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

# Step 1: Read and Clean Graph Data
with open("Friendship_Graph_2022.csv", "r", encoding="utf-8") as infile, open("cleaned_graph.adjlist", "w", encoding="utf-8") as outfile:
    for line in infile:
        clean_line = ",".join([x.strip() for x in line.split(",") if x.strip()])
        outfile.write(clean_line + "\n")

# Step 2: Load Graph
G = nx.read_adjlist("cleaned_graph.adjlist", delimiter=",")

# Step 3: Clean Node Names
G = nx.relabel_nodes(G, lambda x: x.strip().replace("\ufeff", "").replace("\r", ""))

print("Cleaned Nodes:", list(G.nodes))

# Step 4: Remove Specific Node
your_node = "629"
if your_node in G:
    G.remove_node(your_node)
    print(f"Removed node: {your_node}")
else:
    print(f"Node {your_node} not found in graph.")

# Step 5: Handle Disconnected Graph (Keep Largest Connected Component)
if not nx.is_connected(G):  
    components = list(nx.connected_components(G))
    print("Connected Components Sizes:", [len(c) for c in components])

    LCC = max(components, key=len)
    G = G.subgraph(LCC).copy()

plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10)
plt.title("Updated Social Network Graph")
plt.show()

# Step 6: Compute Graph Metrics
degree_dict = dict(G.degree())
clustering_dict = nx.clustering(G)

# Ensure graph is connected for path length computation
if nx.is_connected(G):
    path_length_dict = dict(nx.shortest_path_length(G))
    all_path_lengths = [dist for node in path_length_dict for dist in path_length_dict[node].values() if node != dist]
else:
    all_path_lengths = []

# Step 7: Visualizing Distributions

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Degree Distribution
axes[0].hist(degree_dict.values(), bins=np.arange(0, max(degree_dict.values()) + 1, 1), color='skyblue', edgecolor='black')
axes[0].set_title("Degree Distribution")
axes[0].set_xlabel("Degree")
axes[0].set_ylabel("Frequency")

# Clustering Coefficient Distribution
axes[1].hist(clustering_dict.values(), bins=20, color='lightcoral', edgecolor='black')
axes[1].set_title("Clustering Coefficient Distribution")
axes[1].set_xlabel("Clustering Coefficient")
axes[1].set_ylabel("Frequency")

# Path Length Distribution (if connected)
if all_path_lengths:
    axes[2].hist(all_path_lengths, bins=20, color='lightgreen', edgecolor='black')
    axes[2].set_title("Path Length Distribution")
    axes[2].set_xlabel("Shortest Path Length")
    axes[2].set_ylabel("Frequency")
else:
    axes[2].text(0.5, 0.5, "Graph is not connected", fontsize=14, ha='center')

plt.tight_layout()
plt.show()

# 4 types of centrality measures of all the nodes

degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)

# Convert to DataFrame for easy sorting
centrality_df = pd.DataFrame({
    "Node": list(G.nodes),
    "Degree": degree_centrality.values(),
    "Closeness": closeness_centrality.values(),
    "Betweenness": betweenness_centrality.values(),
    "Eigenvector": eigenvector_centrality.values()
})

# Sort by each centrality measure and take the top 10 nodes
top_10_degree = centrality_df.nlargest(10, "Degree")
top_10_closeness = centrality_df.nlargest(10, "Closeness")
top_10_betweenness = centrality_df.nlargest(10, "Betweenness")
top_10_eigenvector = centrality_df.nlargest(10, "Eigenvector")

# Display results
print("\nTop 10 Nodes by Degree Centrality:\n", top_10_degree)
print("\nTop 10 Nodes by Closeness Centrality:\n", top_10_closeness)
print("\nTop 10 Nodes by Betweenness Centrality:\n", top_10_betweenness)
print("\nTop 10 Nodes by Eigenvector Centrality:\n", top_10_eigenvector)

# Save results to CSV
centrality_df.to_csv("centrality_measures.csv", index=False)

# Plot Degree Distribution
plt.figure(figsize=(10, 5))
degree_values = [deg for _, deg in G.degree()]
plt.hist(degree_values, bins=20, color='skyblue', edgecolor='black')
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degree Distribution of Graph")
plt.show()

communities = list(nx.algorithms.community.asyn_lpa_communities(G))

# Assign a unique color to each community
community_colors = {}
colors = ["#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(len(communities))]

for i, community in enumerate(communities):
    for node in community:
        community_colors[node] = colors[i]

# Draw the graph with different colors for each community
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
nx.draw(G, pos, with_labels=True, node_color=[community_colors[node] for node in G.nodes()], 
        edge_color='gray', node_size=800, font_size=8)

plt.title("Community Detection in Social Network Graph")
plt.show()

clustering_coeff = nx.average_clustering(G)

# Calculate Average Shortest Path Length
avg_path_length = nx.average_shortest_path_length(G)

# Generate a Random Graph with the same number of nodes & edges
random_graph = nx.gnm_random_graph(n=len(G.nodes()), m=len(G.edges()))

# Calculate Clustering & Path Length for Random Graph
random_clustering = nx.average_clustering(random_graph)
random_path_length = nx.average_shortest_path_length(random_graph)

# Display Results
print("🔹 Small-World Network Analysis 🔹")
print(f"Graph Clustering Coefficient: {clustering_coeff:.4f}")
print(f"Random Graph Clustering Coefficient: {random_clustering:.4f}")
print(f"Graph Average Path Length: {avg_path_length:.4f}")
print(f"Random Graph Average Path Length: {random_path_length:.4f}")

# Small-World Condition Check
if clustering_coeff > random_clustering and avg_path_length <= random_path_length:
    print("✅ The Graph Exhibits Small-World Properties!")
else:
    print("❌ The Graph Does NOT Exhibit Small-World Properties.")