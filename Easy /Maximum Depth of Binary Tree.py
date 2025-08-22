# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:  # Check if the root is None
            return 0
        
        queue = []  # Initialize queue for BFS
        queue.append(root)  # Add root node to queue
        lvl = 0  # Initialize level
        
        while queue:
            lvl += 1  # Increment level after processing each depth
            for i in range(len(queue)):
                node = queue.pop(0)  # Pop the first element in the queue (inefficient but works)
                if node.left:
                    queue.append(node.left)  # Add left child to queue
                if node.right:
                    queue.append(node.right)  # Add right child to queue
        
        return lvl
