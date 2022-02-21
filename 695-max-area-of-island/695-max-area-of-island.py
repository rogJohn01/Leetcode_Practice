class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        global al 
        def dfs(x,y):
            global al 
            if x < 0 or x>=len(grid) or y <0 or y>= len(grid[0]) or grid[x][y]!=1:
                return 
            
            grid[x][y] ='#'
            
            al +=1 
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            
        ret = [] 
        cnt = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    al = 0
                    dfs(i,j )
                    cnt +=1
                    ret.append(al)
        return max(ret) if ret else  0