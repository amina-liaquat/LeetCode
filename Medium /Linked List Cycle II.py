# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        f = s = head
        while f and f.next:
            s, f = s.next, f.next.next
            if f == s:
                # return True
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None
        
