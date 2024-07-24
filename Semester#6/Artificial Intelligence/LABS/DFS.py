# -*- coding: utf-8 -*-
"""
Created on Sat May 18 19:14:51 2024

@author: Laiba Binta Tahir
"""

#TASKS
#1. Using DFS find the goal state (Python Implementation).
#2. Implementation of DFS to traverse each node.
#3. Implementation of Sliding puzzle using DFS

# Depth-First Search (DFS) to Find the Goal State
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    if start == goal:
        print("\nGoal state reached:", goal)
        return True
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

# DFS to Traverse Each Node
def dfs_traverse(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_traverse(graph, neighbor, visited)

# Sliding Puzzle Using DFS
from collections import deque

# Helper function to generate possible moves
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = divmod(index, 3)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

def dfs_puzzle(start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        
        if state == goal:
            print("Goal state reached!")
            for step in path:
                print(step)
            return
        
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    
    print("Goal state not reachable")

# Graph example
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : ['G'],
    'G' : ['H', 'I'],
    'H' : [],
    'I' : []
}

# Example start and goal states for the sliding puzzle
start_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # Representing the puzzle as a tuple
goal_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)

# Driver code for DFS to find the goal state
print("DFS to find the goal state:")
dfs(graph, 'A', 'G')
print("\n")

# Driver code for DFS to traverse each node
print("DFS to traverse each node:")
dfs_traverse(graph, 'A')
print("\n")

# Driver code for Sliding Puzzle using DFS
print("Sliding puzzle using DFS:")
dfs_puzzle(start_state, goal_state)
