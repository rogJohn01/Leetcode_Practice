class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        d =[ [1]*n for _ in range(m)]
        
        for r in range(1,m):
            for c in range(1,n):
                d[r][c] = d[r-1][c] + d[r][c-1]
        return d[m-1][n-1]
       