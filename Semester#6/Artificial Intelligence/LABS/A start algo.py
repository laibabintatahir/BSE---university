# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:11:19 2024

@author: Laiba Binta Tahir
"""

#A* SEARCH ALGORITHM
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Create a graph
G = nx.Graph()
nodes = range(1, 8)
edges = [
    (1, 2, {'cost': 1}), 
    (1, 3, {'cost': 3}), 
    (2, 4, {'cost': 3}),
    (3, 5, {'cost': 2}), 
    (4, 6, {'cost': 1}), 
    (5, 6, {'cost': 2}),
    (5, 7, {'cost': 3}), 
    (6, 7, {'cost': 1})
]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Define the heuristic values for each node
heuristics = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0}

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
                heapq.heappush(heap, (len(path) + heuristics[neighbor], neighbor, path + [neighbor]))

# Define start and goal nodes
start_node = 1
goal_node = 7
best_path = astar_search(G, start_node, goal_node, heuristics)
print(best_path)


# Visualize the graph with the best path
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=4000, node_color='LightBlue', font_weight='bold')

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

plt.title("A* Search on Simplified Graph")
plt.show()
