# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        
            p = head 
            ix = 1
            arr = []  
            while True: 
                if left <= ix: 
                    arr.append(p.val)
                if ix ==right: 
                    break 
                p = p.next 

                ix +=1 

            arr.reverse() 

            p = head
            ix =1 ; px = 0 
            while True: 
                if left <= ix <=right: 
                    p.val = arr[px]
                    px +=1 
                if ix ==right:
                    break 
                p = p.next 
                ix +=1 
            return head 
