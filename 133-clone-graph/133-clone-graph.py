"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        
        visited = {}
        queue =deque([node])
        
        visited[node] = Node(node.val , []) 
        
        while queue:
            
            n = queue.popleft()
            
            for ne in n.neighbors:
                if ne not in visited:
                    
                    visited[ne] = Node(ne.val ,[] )
                    
                    queue.append(ne)
                visited[n].neighbors.append(visited[ne])
        return visited[node]
        