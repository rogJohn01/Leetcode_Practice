# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        ans = []
        if not root: return ans

        def dfs(node,dep):
            if len(ans) == dep:
                ans.append([])

            ans[dep].append(node.val)

            if node.left: dfs(node.left ,dep+1)
            if node.right: dfs(node.right ,dep+1)

        dfs(root, 0)
        return ans[::-1]
                