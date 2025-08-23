# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        # heapq.heapify(heap)

        def findKth(root):
            if not root:
                return
            
            heapq.heappush(heap, -1 * root.val)
            if len(heap) > k:
                heapq.heappop(heap)

            findKth(root.left)
            findKth(root.right)
        
        findKth(root)
        return -1 * heapq.heappop(heap)
        
