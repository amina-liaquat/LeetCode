from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        q = deque([(root, 1)]) # root node , level of the node

        while q:
            node , depth = q.popleft() # we remove the node and get the value and level

            if not node.left and not node.right:
                return depth
            
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
