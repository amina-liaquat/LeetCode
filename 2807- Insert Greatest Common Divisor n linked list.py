# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(num1,num2):
        div=min(num1,num2)
        while num1%div!=0 or num2%div!=0:
            div-=1
        return div
        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        
        prev=head
        temp=head.next
        div=0

        while temp!=None:
            div=gcd(prev.val,temp.val)
            node=ListNode(div,prev.next)
            prev.next=node
            prev=temp
            temp=temp.next

        return head
