class Solution:
    def findPaths(self, R: int, C: int, maxMove: int, sx: int, sy: int) -> int:
        
        @lru_cache(None) 
        def dfs(x,y , mleft): 

            if not(	0<= x < R and 0 <= y <C):
                return 1 
            if not mleft:   return 0 

            ans = 0 
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:  
                nx, ny =  x+a , y+b 
                ans = ( ans + dfs(nx,ny, mleft-1 )) % 1000000007
            return ans 

        return dfs(sx,sy, maxMove) 

