# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = collections.deque()
        q.append(root)

        while q:
            same_lvl = []

            for i in range(len(q)):
                node = q.popleft()
                same_lvl.append(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(same_lvl)
        
        return res






