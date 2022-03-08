class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        N = len(A)
        seen = set()

        def dfs(node):

            for i , v in enumerate(A[node]):
                if v and i not in seen:
                    seen.add(i)
                    dfs(i)



        ans = 0 
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans +=1 
        return ans 