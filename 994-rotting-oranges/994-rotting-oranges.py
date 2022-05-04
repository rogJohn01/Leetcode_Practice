class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
            def bfs():

                while q:
                    x,y = q.popleft() 
                    for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
                        nx , ny = x+a ,y+b

                        if 0<=nx < R and 0<=ny < C:
                            if grid[nx][ny] =='#':
                                grid[nx][ny] = grid[x][y] +1 
                                q.append((nx,ny))

            R = len(grid) ; C = len(grid[0])
            if R == C ==1:
                if grid[-1][-1] ==1:
                    return -1 
                return 0
            orangeBox = []
            q = deque()
        
            for r in range(R):
                for c in range(C):
                    if grid[r][c] ==2:
                        q.append([r,c])
                    elif grid[r][c] ==1:
                        grid[r][c] = '#'

            bfs()
            maxv= 0 
            for r in range(R):
                for c in range(C):
                    if grid[r][c] =='#':
                        return -1
                    elif maxv < grid[r][c]:
                        maxv = grid[r][c]
                        
            return maxv -2 if maxv !=0 else 0 