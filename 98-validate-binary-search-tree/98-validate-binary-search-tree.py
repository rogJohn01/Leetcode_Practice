# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
       
        inf = float('inf') 
        st = [ [root, -inf , inf] ] 
        while st: 

            node , lw , up = st.pop()
            if not node: continue 
            v = node.val
            if v <= lw or v>= up: 
                return False 
            st.append([node.right , v , up])
            st.append([node.left , lw , v ])

        return True 