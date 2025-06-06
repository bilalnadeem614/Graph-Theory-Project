# Social Network Graph Analysis

## Overview
This project analyzes a social network graph using **NetworkX** and **Matplotlib** in Python. The analysis includes:
- Cleaning and visualizing the graph
- Computing various graph statistics
- Finding centrality measures
- Detecting communities
- Checking for small-world properties
- Generating distributions of node properties

## Features
### 1. **Graph Cleaning & Visualization**
- Reads a CSV file and removes unwanted characters.
- Converts the data into an adjacency list format.
- Visualizes the cleaned graph with labels.

### 2. **Graph Properties**
The following network properties are computed:
- **Average Degree**
- **Average Clustering Coefficient**
- **Average Path Length**
- **Graph Diameter**
- **Assortativity Coefficient**
- **Nodes with Highest & Lowest Degree**

### 3. **Degree, Clustering Coefficient & Path Length Distribution**
- Generates distribution plots for:
  - Node degrees
  - Clustering coefficients
  - Path lengths

### 4. **Centrality Measures (Top-10 Nodes)**
- **Degree Centrality**
- **Closeness Centrality**
- **Betweenness Centrality**
- **Eigenvector Centrality**

### 5. **Community Detection**
- Uses the **asyn_lpa_communities** method from NetworkX to identify communities.
- Visualizes the graph with different colors for each community.

### 6. **Small-World Property Check**
- Compares the clustering coefficient and path length to determine if the graph exhibits small-world behavior.

## Installation & Usage
### Prerequisites
- Python 3.x
- NetworkX
- Matplotlib
- Pandas (optional, for advanced data handling)

### Installation
```bash
pip install networkx matplotlib
```

### Run the Script
```bash
python analysis.py
```
## Author
**Muhammad Talha** 
