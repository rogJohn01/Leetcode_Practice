class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:


        def dfs(x,y):

            if dp[x][y]: 
                return dp[x][y] 

            dp[x][y] =1 
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny =  x+a , y+b 
                if 	0<= nx < R and 0 <= ny <C and mat[x][y] < mat[nx][ny]:
                    dp[x][y] = max(dp[x][y] , dfs(nx,ny) +1 ) 
            return dp[x][y] 


        ans = 0 
        R = len(mat) ; C = len(mat[0]) 
        dp = [ [0]*C for _ in range(R) ] 
        for r in range(R):
            for c in range(C):
               ans = max(ans , dfs(r,c))  

        return ans 