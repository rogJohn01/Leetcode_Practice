# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return 

        q = deque()
        q.append( (root ,0))
        record = defaultdict(list) 
        while q: 
            node , dep = q.popleft()
            record[dep].append(node.val)

            if node.left:
               q.append((node.left,dep+1))
            if node.right: 
                q.append((node.right , dep+1))

        ans = [] 
        for i in range(len(record.keys())):
            if i % 2 ==0: 
                ans.append( record[i])
            else: 
                ans.append(record[i][::-1])
        return ans 