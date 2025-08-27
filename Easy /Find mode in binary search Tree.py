# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        curr_count = 0 
        max_count = 0
        nodes = []

        def dfs(node):
            nonlocal prev, curr_count, max_count, nodes
            if not node:
                return
            dfs(node.left)  # inorder: left
            # process current node
            if prev == node.val:
                curr_count += 1
            else:
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
                nodes = [node.val]
            elif curr_count == max_count:
                nodes.append(node.val)
            prev = node.val  # update previous value
            dfs(node.right)  # inorder: right
        dfs(root)
        return nodes







        
