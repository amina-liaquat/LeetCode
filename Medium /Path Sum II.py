# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # blue print for dfs

        self.ans = [] # array of array

        def dfs(node, path, sm):
            if not root:
                return []
            sm += node.val
            # tmp = path + [node.val] #deep copy
            path.append(node.val)
            if not node.left and not node.right and sm == targetSum:
                self.ans.append(list(path))
            if node.left:
                dfs(node.left, path, sm)
            if node.right:
                dfs(node.right, path, sm)
            path.pop()

        dfs(root, [], 0) # root, pathArray, sum
        return self.ans

# deep copy
# array/ object reference based
