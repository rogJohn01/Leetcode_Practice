# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        g = defaultdict(list)
        q = [(root,0)]
        while q: 
            new = [] 
            d = defaultdict(list) 
            for node,x in q: 
                d[x].append(node.val) 
                if node.left: new += (node.left , x-1) , 
                if node.right: new += (node.right , x+1) ,
            for i in d: 
                g[i].extend(sorted(d[i]))
            q = new 
        return [ g[i] for i in sorted(g)] 

