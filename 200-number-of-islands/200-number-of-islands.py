class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count
    
    def is_valid(self, grid,x,y):
        m, n = len(grid) , len(grid[0])
        if x < 0 or y < 0 or x>= m or y >= n:
            return False
        return True 
    
    def bfs(self,grid ,x,y):
        
        queue = deque()
        queue.append((x,y))
        grid[x][y] ='0'
        
        while queue:
            x, y = queue.popleft()
            direct = [(0,1),(0,-1), (-1,0) , (1,0) ] 
            for d in direct:
                nx , ny = x+d[0] , y+d[1]
                
                if self.is_valid(grid, nx,ny) and grid[nx][ny] =='1':
                    queue.append((nx,ny))
                    grid[nx][ny] = '0'
                             
                             