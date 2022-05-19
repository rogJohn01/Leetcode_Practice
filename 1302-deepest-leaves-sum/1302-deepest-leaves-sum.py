# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        


        q = deque([(root, 0),] ) 
        maxdep = 0 
        totv = 0 
        while q: 

            node , dep = q.popleft() 

            if node.left is None and node.right is None: 

                if maxdep < dep:
                    maxdep = dep 
                    totv = node.val         

                elif  maxdep ==dep: 
                    totv += node.val 


            else:

                if node.left:
                    q.append([node.left , dep+1 ]) 
                if node.right: 
                    q.append([node.right , dep+1 ]) 

        return totv 