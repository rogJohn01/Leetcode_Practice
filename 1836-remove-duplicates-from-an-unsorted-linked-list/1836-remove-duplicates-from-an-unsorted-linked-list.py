# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        
            dic = defaultdict(int)
            curr = head 
            
            while curr:
                dic[curr.val] +=1 
                curr = curr.next 
            print(dic)
            
            dummy = ListNode()
            dummy.next = head 
            prev = dummy 
            print(head.val)
            while head:
                if dic[head.val] >1:
                    prev.next = head.next 
                else:
                    prev = prev.next 
                head = head.next 
            return dummy.next 
                    