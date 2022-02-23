class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        
        # use normalization ! to find the same! 
        def dfs(x,y):

            if x < 0 or x >=R or y <0 or y>=C:
                return 
            if (x,y) in seen or not grid[x][y]:
                return 

            seen.add((x,y))
            curLand.add((x-rorigin, y- corigin))
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(x+a,y+b)




        seen = set()
        uniLand = set()
        R = len(grid) ; C = len(grid[0])
        for i in range(R):
            for j in range(C):
                curLand = set()
                rorigin = i
                corigin = j 
                dfs(i,j)
                if curLand:
                    uniLand.add( frozenset(curLand))
        return len(uniLand)
