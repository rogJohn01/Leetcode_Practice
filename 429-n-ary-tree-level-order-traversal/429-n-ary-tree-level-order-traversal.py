"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        ans = [] 
        if not root: return ans 
        
        def dfs(node,dep):
            
            if len(ans) == dep:
                ans.append([])
            
            ans[dep].append(node.val)
            for child in node.children: 
                dfs(child,dep+1)
        
        dfs(root,0)
        return ans 
    
    
        