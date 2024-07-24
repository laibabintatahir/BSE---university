# -*- coding: ut f-8 -*-
"""
Created on Mon May 20 17:35:12 2024

@author: Laiba Binta Tahir
"""

#BEST FIRST SEARCH
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph
G = nx.Graph()
G.add_nodes_from(range(1, 7))
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 6), (5, 6)])

# Define the heuristic values for each node
heuristics = {1: '5', 2: '4', 3: '2', 4: '3', 5: '1', 6: '0'}

# Implement Best First Search algorithm
def best_first_search(graph, start, goal, heuristics):
    visited = []
    queue = [(start, [start])]

    while queue:
        node, path = queue.pop(0)
        visited.append(node)

        if node == goal:
            return path

        neighbors = sorted(graph.neighbors(node), key=lambda x: heuristics[x])
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

# Find the best path
start_node = 1
goal_node = 6
best_path = best_first_search(G, start_node, goal_node, heuristics)
print(best_path)

# Define the positions of the nodes for visualization
pos = {1: (1, 3), 2: (2, 4), 3: (2, 2), 4: (3, 5), 5: (3, 1), 6: (4, 3)}

# Draw the graph
nx.draw(G, pos, with_labels=False, node_size=1000, node_color='lightblue')

# Draw heuristic values near nodes
nx.draw_networkx_labels(G, pos, labels={node: f"{node}\n({heuristics[node]})" for node in G.nodes()}, font_size=12, font_color='black', verticalalignment='center')

# Highlight the best path in red
nx.draw_networkx_nodes(G, pos, nodelist=best_path, node_color='red', node_size=1000)
nx.draw_networkx_edges(G, pos, edgelist=[(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)], edge_color='red', width=2)

# Add title and show the plot
plt.title("Best First Search")
plt.show()
