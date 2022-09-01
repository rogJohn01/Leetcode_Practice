# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        st = [[root , float('-inf')]]
        ans = 0 
        
        while st: 
            node , maxsf = st.pop() 
            if maxsf <= node.val: 
                ans +=1 
            
            if node.left:

                st.append([node.left , max(node.val ,maxsf)])
            if node.right: 

                st.append([node.right , max(node.val ,maxsf)] )
        return ans 
    
    