# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:34:01 2024

@author: Laiba Binta Tahir
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = range(1, 11)
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6), (5, 7), (6, 7), (6, 8), (8, 9), (8, 10)]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G)
nx.draw(G,pos,  with_labels=True, node_size=500, node_color='pink') 
plt.show()
