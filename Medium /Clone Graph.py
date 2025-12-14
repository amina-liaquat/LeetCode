"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        visited = {}
        queue = deque()

        c_node = Node(node.val)

        visited[node] = c_node
        queue.append(node)       

        while queue:
            curr = queue.popleft()

            for neib in curr.neighbors:
                if neib not in visited:
                    clone_neib = Node(neib.val)                   
                    visited[neib] = clone_neib
                    queue.append(neib)

                visited[curr].neighbors.append(visited[neib])

        return visited[node] 
