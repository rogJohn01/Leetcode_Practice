# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return 
        st = [root]
        path = [] 
        
        while st:
            node = st.pop()
            
            path.append( node.val)
            
            if node.left: 
                st.append(node.left)
            if node.right:
                st.append(node.right)
        
        return path[::-1]