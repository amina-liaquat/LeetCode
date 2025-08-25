# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        first_head = head
        sec_head = head.next

        temp1 = first_head
        temp2 = sec_head

        while temp1 and temp2 and temp2.next:

            temp1.next = temp2.next 
            temp2.next = temp2.next.next

            temp1 = temp1.next
            temp2 = temp2.next
        
        temp1.next = sec_head
        return first_head
        
