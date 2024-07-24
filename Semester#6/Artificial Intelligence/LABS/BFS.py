# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:12:32 2024

@author: Laiba Binta Tahir
"""
#BREADTH FIRST SEARCH
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['H', 'I'],
    'E' : [],
    'F' : ['G'],
    'G' : [],
    'H' : [],
    'I' : []
}

visited = [] # List to keep track of visited nodes.
queue = []   # Initialize a queue

def bfs(visited, graph, node, goal):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")

        if s == goal:
            print("\nGoal state reached:", goal)
            return

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A', 'G')
