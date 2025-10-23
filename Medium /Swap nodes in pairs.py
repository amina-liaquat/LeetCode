# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy node
        point dummy.next =head
        while
        swaping
        return dummy.next

        """
        dummy =ListNode(0) 
        
        dummy.next=head  #
        prev,curr=dummy,head
        while curr and curr.next :
            # save ptrs
            nxtpair=curr.next.next
            second=curr.next

            # reverse the paris
            second.next=curr
            curr.next=nxtpair

            prev.next=second

            prev=curr
            curr=nxtpair
        return dummy.next

        #T: O(n)
        #S:O(1)
