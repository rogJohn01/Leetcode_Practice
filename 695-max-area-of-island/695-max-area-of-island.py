class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        from collections import deque 

      
        def bfs(x,y ):

            queue = deque()
            queue.append((x,y))
            dx = [1,-1,0,0] 
            dy = [0,0,1,-1]
            grid[x][y] ='#'
            cnt = 0 
            while queue:
                x, y  = queue.popleft()
                cnt +=1 
                for i in range(4):
                    nx = x +dx[i]
                    ny = y +dy[i]
                    if nx <0 or nx >=R or ny<0 or ny>=C or grid[nx][ny] !=1:
                        continue 
                    if grid[nx][ny] ==1:
                        queue.append((nx,ny))
                        grid[nx][ny] ='#'
            return cnt 

        R = len(grid) ; C = len(grid[0])
        ans =0 
        for r  in range(R):
            for c in range(C):
                if grid[r][c] ==1:
                    ans = max(ans, bfs(r,c))

        return ans 