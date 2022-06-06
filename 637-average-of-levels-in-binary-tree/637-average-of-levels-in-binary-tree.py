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
        dic = defaultdict(int)
        cntd = defaultdict(int)
        while st: 
            node , dep = st.pop()
            
          
            dic[dep] += node.val 
            cntd[dep] +=1 
            
            if node.left: 
                st.append([node.left, dep+1])
            if node.right:
                st.append([node.right ,dep+1])
        mdep = max(dic.keys())
        for d in range(mdep+1):
            dic[d] /= cntd[d]
        for k ,v in dic.items():
            ans.append(v)
        return ans 