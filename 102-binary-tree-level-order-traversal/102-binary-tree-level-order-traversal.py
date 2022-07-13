# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        
        if root is None: 
            return [] 
        
        q = deque()
        q.append([root,0])
        dic = defaultdict(list)
        ans = [] 
        
        while q: 
            
            node,dep = q.popleft() 
            dic[dep].append(node.val)
            if node.left:
                q.append([node.left,dep+1])
            
            if node.right: 
                q.append([node.right,dep+1])
         
        return [ v for k,v in dic.items() ]