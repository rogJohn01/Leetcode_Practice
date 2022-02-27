# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0 
        maxWid = 0 
        
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            levLen = len(queue)
            _, levheadIdx = queue[0]
            for _ in range(levLen):
                node , colIndex = queue.popleft()
                
                if node.left:
                    queue.append((node.left,2*colIndex))
                if node.right:
                    queue.append((node.right, 2*colIndex+1))
            
            maxWid = max( maxWid, colIndex-levheadIdx+1)
        return maxWid 