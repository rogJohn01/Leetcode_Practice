# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        st = [root]
        arr = [] 
        while st: 
            node = st.pop()
            arr.append(node.val)
            if node.left: 
                st.append(node.left)
            if node.right:
                st.append(node.right)
        arr.sort() 
        ans = float('inf')
        for i in range(1,len(arr)): 
            if arr[i] - arr[i-1] < ans: 
                ans = arr[i] - arr[i-1]
        return ans 
            
            
            
    
    