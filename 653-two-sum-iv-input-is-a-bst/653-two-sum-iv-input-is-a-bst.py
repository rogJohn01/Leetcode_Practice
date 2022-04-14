# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        

        if not root:
            return False 

        bfs , s = [root] , set()

        for node  in bfs:
            if k - node.val in s:
                return True 
            s.add(node.val) 
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return False 


