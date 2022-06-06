# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        

        st = [[root,0]]
        ans = []
        cntr = [] 
        while st:
            node , dep = st.pop()

            if dep+1 > len(ans):
                ans.append(0)
            if dep+1 > len(cntr): 
                cntr.append(0)
            cntr[dep] +=1
            ans[dep] += node.val 
            if node.left:
                st.append([node.left, dep+1])
            if node.right:
                st.append([node.right ,dep+1])
        for d in range(len(ans)):
            ans[d] /= cntr[d]
        return ans