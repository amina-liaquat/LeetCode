class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            return (r1.val == r2.val) and isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left)
        if root:
            return isMirror(root.left,root.right)
        return True
