"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return [] 
        
        st = [root] 
        path = [] 
        while st:
            node = st.pop() 
            path.append(node.val) 
            st.extend(node.children[::-1])
                
        return path