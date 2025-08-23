# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
   def mergeTwoLists(self, list1, list2):
       dummy = ListNode()
       cur = dummy

       while list1 and list2:
           if list1.val > list2.val:
               cur.next = list2
               list2 = list2.next
           else:
               cur.next = list1
               list1 = list1.next
           
           cur = cur.next
       
       if list1:
           cur.next = list1
       else:
           cur.next = list2
       
       return dummy.next
