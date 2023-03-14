# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        box = [] 
        tmp = [] 
        st = [(root, "0") ]
        
        while st: 
            
            node ,path  = st.pop()
            path += str(node.val)
            if not node.left and not node.right: 
                box.append(path)
            
            
            if node.left:
                st.append( [node.left , path])
            if node.right: 
                st.append( [node.right , path ])
               
        ans = 0 
        for b in box: 
            ans += int(b)
        
        return ans 