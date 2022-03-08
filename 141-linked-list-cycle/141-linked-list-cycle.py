# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        
        visit = set()
        while head is not None:

            if head in visit:
                return True 
            visit.add(head)
            head = head.next 
        return False 