# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:


        def bfs(root): 


            st = [root] 
            ans = [] 
            while st: 
                node = st.pop() 
                if node.left: 
                    st.append(node.left)
                if node.right: 
                    st.append(node.right) 
                if not node.left and not node.right: 
                    ans.append(node.val) 

            return ans 

        return bfs(root1) == bfs(root2)
