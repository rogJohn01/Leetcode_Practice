# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
        vals = [] 
        h =head 
        
        while h is not None:
            vals.append(h.val)
            h = h.next 
        return vals == vals[::-1]