# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return 
        dic = defaultdict(list)
        q = deque()
        q.append([root,0])
        
        while q: 
            node,dep = q.popleft() 
            dic[dep].append(node.val)
            
            if node.left: 
                q.append([node.left ,dep+1])
            
            if node.right:
                q.append([node.right, dep+1])
        
        return [ v[-1] for k,v in dic.items() ] 