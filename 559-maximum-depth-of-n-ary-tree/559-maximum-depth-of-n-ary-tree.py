"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None:
            return 0
        
        st = [(root,0),] 
        dep = maxdep = 0
        
        while st: 
            
            node , dep = st.pop()
            
            if node.children == []: 
                if dep > maxdep:
                    maxdep = dep 
            
            else: 
                for child in node.children:
                    st.append([child, dep+1])
                
                
        return maxdep +1 