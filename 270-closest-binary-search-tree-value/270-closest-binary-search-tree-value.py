# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        minv = float('inf')
        while root is not None and root.val !=target:
            if abs(root.val- target) < minv:
                minv = abs(root.val- target)
                ans = root.val
            
            root = root.left if target < root.val else root.right 
            
            
        if root is not None and root.val ==target:
            ans = root.val 
            
        return ans 