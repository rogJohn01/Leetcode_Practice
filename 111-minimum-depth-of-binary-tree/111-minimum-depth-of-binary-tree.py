# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0 
        mindep = float('inf')
        st = [ (root,0)]
        
        while st: 
            
            node , dep = st.pop()
            
            if node.left is None and node.right is None:
                if dep < mindep:
                    mindep = dep 
            
            else:
                if node.left:
                    st.append([node.left ,dep+1])
                if node.right:
                    st.append([node.right ,dep+1])
        return mindep +1 