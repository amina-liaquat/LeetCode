class Solution:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = None

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # if order is wrong
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node
            inorder(node.right)

        inorder(root)

        # swap the wrong values
        self.first.val, self.second.val = self.second.val, self.first.val
