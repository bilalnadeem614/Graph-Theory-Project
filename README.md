# 📊 Graph Theory Project: Social Network Analysis of CS-22 Students

This project analyzes the social network of CS-22 students using graph theory techniques to uncover key insights into the structure and dynamics of their relationships. By constructing a graph from a CSV file and applying various network science algorithms, we explore centrality, clustering, community structure, and small-world properties.

---

## 🧩 Features

### 🔨 Graph Construction & Preprocessing
- Reads raw data from `Friendship_Graph_2022.csv` and cleans it into an adjacency list format.
- Builds the graph using NetworkX.
- Cleans malformed node names (e.g., removes BOM characters, whitespace).
- Optionally removes a specified node (e.g., `"629"`).

### 🔍 Structural Analysis
- Focuses analysis on the **Largest Connected Component** to ensure graph connectivity.
- **Degree Distribution:** Analyzes how many connections each student has.
- **Clustering Coefficient Distribution:** Measures local group cohesion.
- **Shortest Path Length Distribution:** Analyzes the distance between nodes (if the graph is connected).

### 📈 Centrality Measures
Computes the following centrality metrics for all nodes:
- **Degree Centrality**
- **Closeness Centrality**
- **Betweenness Centrality**
- **Eigenvector Centrality**

Top 10 students for each metric are extracted and saved to a CSV file (`centrality_measures.csv`).

### 🧠 Community Detection
- Uses the **Asynchronous Label Propagation Algorithm (LPA)** to detect social clusters.
- Visualizes communities with unique colors.

### 🌐 Small-World Property Assessment
- Compares average clustering coefficient and path length of the graph to a random graph of the same size.
- Determines whether the network exhibits **small-world behavior**.

---

## 📊 Visualizations

- Graph visualizations (cleaned graph, community-colored network).
- Histograms of:
  - Degree distribution
  - Clustering coefficients
  - Path lengths

---

## 🛠 Technologies Used

- **Python**
- **Jupyter Notebook**
- **NetworkX** – Network creation and analysis
- **Pandas** – Data manipulation and export
- **NumPy** – Numerical analysis
- **Matplotlib** – Plotting and visualizations

---

## ▶️ How to Run

1. Ensure the file `Friendship_Graph_2022.csv` is in the working directory.
2. Run `Graph.py` or execute the steps in `SNA.ipynb` to generate graphs and analysis.
3. Output files:
   - `cleaned_graph.adjlist`
   - `centrality_measures.csv`

---

## 📚 Output Summary

- Cleaned social graph
- Centrality leaderboards
- Cluster visualizations
- Confirmation of small-world properties (if applicable)

---
