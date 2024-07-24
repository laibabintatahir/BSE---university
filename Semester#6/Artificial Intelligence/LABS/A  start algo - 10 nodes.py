# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:15:09 2024

@author: Laiba Binta Tahir
"""

# A* search algorithm with a graph containing 10 nodes,
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Create a graph with 10 nodes and multiple connections
G = nx.Graph()
nodes = range(1, 11)
edges = [
    (1, 2, {'cost': 4}), 
    (1, 3, {'cost': 2}), 
    (2, 4, {'cost': 5}),
    (2, 5, {'cost': 10}),
    (3, 6, {'cost': 3}), 
    (4, 7, {'cost': 4}), 
    (5, 8, {'cost': 6}),
    (6, 7, {'cost': 1}),
    (7, 8, {'cost': 2}), 
    (8, 9, {'cost': 8}),
    (9, 10, {'cost': 7}),
    (6, 10, {'cost': 9}),
    (1, 10, {'cost': 15}),
]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define heuristic values for each node
heuristics = {1: 14, 2: 13, 3: 11, 4: 7, 5: 10, 6: 4, 7: 3, 8: 6, 9: 2, 10: 0}

# Implement A* search algorithm
def astar_search(graph, start, goal, heuristics):
    visited = set()
    heap = [(0 + heuristics[start], start, [start])]
    
    while heap:
        _, node, path = heapq.heappop(heap)
        
        if node in visited:
            continue
            
        if node == goal:
            return path
            
        visited.add(node)
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_cost = len(path) + heuristics[neighbor]
                heapq.heappush(heap, (new_cost, neighbor, path + [neighbor]))

# Define start and goal nodes
start_node = 1
goal_node = 10
best_path = astar_search(G, start_node, goal_node, heuristics)

# Visualize the graph with the best path
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='LightBlue', font_weight='bold')

# Draw edge costs on edges
edge_labels = {(u, v): f"cost:{d['cost']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Draw heuristic values near nodes
nx.draw_networkx_labels(G, pos, labels={node: f"H:{heuristics[node]}\nN:{node}" for node in G.nodes()}, font_size=12, font_color='black', verticalalignment='center')

# Highlight start and goal nodes
nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='green', node_size=2000)
nx.draw_networkx_nodes(G, pos, nodelist=[goal_node], node_color='red', node_size=2000)

# Highlight best path
nx.draw_networkx_nodes(G, pos, nodelist=best_path, node_color='blue', node_size=2000)
nx.draw_networkx_edges(G, pos, edgelist=[(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)], edge_color='blue', width=2)

plt.title("A* Search on 10-Nodes Graph")
plt.show()
