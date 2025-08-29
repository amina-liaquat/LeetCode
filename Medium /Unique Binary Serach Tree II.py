# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]  # empty tree

            all_trees = []

            for i in range(start, end + 1):
                # Generate all left and right subtrees
                left_trees = build(start, i - 1)
                right_trees = build(i + 1, end)

                # Combine them with root i
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)

            return all_trees

        return build(1, n)
