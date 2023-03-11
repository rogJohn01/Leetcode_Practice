# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        
        node = head
        arr = [] 
        while node: 
            arr.append( node.val)
            node = node.next 

        print(arr)
        def bst(arr):
            
            if not arr: return None 
            
            m = len(arr) //2 
            node = TreeNode(arr[m])
            node.left = bst(arr[:m])
            node.right = bst(arr[m+1:]) # the index
            
            return node 
        
        return bst(arr)