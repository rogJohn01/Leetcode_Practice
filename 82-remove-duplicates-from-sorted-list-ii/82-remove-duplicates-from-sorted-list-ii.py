# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        dic = defaultdict(int)
        cur = head 
        while cur:
            dic[cur.val] +=1
            cur = cur.next 
        
        dummy = ListNode()
        dummy.next = head 
        prev = dummy 
        
        while head:
            if dic[head.val] >1:
                prev.next = head.next 
            else:
                prev = prev.next 
            head = head.next 
        return dummy.next 