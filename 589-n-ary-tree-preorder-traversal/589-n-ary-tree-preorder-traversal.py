"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        
        newlist = []
        def traverse(root):
            if root:
                newlist.append(root.val)
                for child in root.children:
                    traverse(child)
                
        traverse(root)
        return newlist