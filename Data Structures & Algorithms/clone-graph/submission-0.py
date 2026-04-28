"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        def dfs(original_node):
            if original_node in visited:
                return visited[original_node]
            
            new_node = Node(original_node.val)
            visited[original_node] = new_node

            for neighbor in original_node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)
            
            return new_node
        
        return dfs(node)
        