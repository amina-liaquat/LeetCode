# Definition for singly-linked list (for reference).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums, head):
        nums = set(nums)
        prev = None
        cur = head
        while cur is not None:
            if cur.val in nums:
                if prev is None:
                    head=head.next
                    cur =head
                else:
                    prev.next=cur.next
                    cur = prev.next
            else:
                prev=cur
                cur=cur.next
        return head
