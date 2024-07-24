"""Created on Mon Apr 29 11:56:03 2024

@author: Laiba Binta Tahir
"""
#MinMaz Algo 

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def build_tree():
    # Leaf nodes
    leaf_values = [
        [5, 6],
        [7, 4, 5],
        [3],
        [6],
        [6, 9],
        [7],
        [5],
        [9, 8],
        [6]
    ]
    
    # Convert leaf values to leaf nodes
    leaf_nodes = [Node(value) for values in leaf_values for value in values]
    
    # Build the tree structure
    root = Node('Max')
    
    # First max level
    max1 = Node('Max')
    min1 = Node('Min')
    min1.add_child(leaf_nodes[0])
    min1.add_child(leaf_nodes[1])
    max1.add_child(min1)
    min2 = Node('Min')
    min2.add_child(leaf_nodes[2])
    max1.add_child(min2)
    root.add_child(max1)
    
    # Second max level
    max2 = Node('Max')
    min3 = Node('Min')
    min3.add_child(leaf_nodes[3])
    max2.add_child(min3)
    min4 = Node('Min')
    min4.add_child(leaf_nodes[4])
    min4.add_child(leaf_nodes[5])
    max2.add_child(min4)
    root.add_child(max2)
    
    # Third max level
    max3 = Node('Max')
    min5 = Node('Min')
    min5.add_child(leaf_nodes[6])
    max3.add_child(min5)
    min6 = Node('Min')
    min6.add_child(leaf_nodes[7])
    min6.add_child(leaf_nodes[8])
    max3.add_child(min6)
    root.add_child(max3)
    
    return root

def draw_tree(node, level=0):
    if node:
        print(" " * (level * 4) + "|-- " + str(node.value))
        for child in node.children:
            draw_tree(child, level + 1)

def min_max(node, depth, max_player):
    if depth == 0 or not node.children:
        return max(node.value) if isinstance(node.value, list) else node.value

    if max_player:
        value = float('-inf')
        for child in node.children:
            value = max(value, min_max(child, depth - 1, False))
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, min_max(child, depth - 1, True))
        return value

# Driver code
if __name__ == "__main__":
    tree = build_tree()
    
    print("Tree structure:")
    draw_tree(tree)
    
    # Find optimal value using Min-Max algorithm
    optimal_value = min_max(tree, depth=3, max_player=True)
    print("Optimal Value:", optimal_value)
