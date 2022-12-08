# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:



        def dfs(node, ans):


            if not node.left and not node.right: 
                ans.append(node.val) 

            if node.left:
                dfs(node.left ,ans)
            if node.right: 
                dfs(node.right , ans)

        ans1 = [] ;  ans2 = [] 
        dfs(root1,ans1 )
        dfs(root2 , ans2 ) 
        return ans1 == ans2 

