class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:

        if len(mat) ==1:
            return mat[-1][-1]

        R = len(mat) ; C = len(mat[0]) 
        dp = [  [0]*C for _ in range(R)  ] 
        dp[0] = mat[0] 

        for r in range(1,R):
            for c in range(C):
                if c ==0:
                    dp[r][c] = mat[r][c] +  min(dp[r-1][1:]) 
                elif c== C-1:
                    dp[r][c] = mat[r][c] + min(dp[r-1][:-1]) 
                else:
                    dp[r][c] = mat[r][c] + min( dp[r-1][:c] + dp[r-1][c+1:] ) 


        return min(dp[R-1])

