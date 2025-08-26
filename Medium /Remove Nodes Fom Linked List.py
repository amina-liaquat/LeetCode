# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        cur = head
        while cur:
            while stack and stack[-1] < cur.val:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next


        dummy = ListNode()
        cur = dummy
        for val in stack:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
        
