# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
        
        p = head
        ar = [] 
        
        while p:
            ar.append(p.val)
            p = p.next 
            
        l , r = 0 , len(ar)-1
        while l < r:
            if ar[l] != ar[r]:
                return False 
            l +=1 ; r -=1 
        return True 
            