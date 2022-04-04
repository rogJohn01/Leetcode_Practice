class Solution:
    def getFood(self, grid:List[List[str]]) -> int:
        
       

        rows = len(grid)
        cols = len(grid[0])
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    q = collections.deque([])
                    q.append((row, col, 0))
                    grid[row][col] = 0
                    while q:
                        r, c, d = q.popleft()
                        for y, x in directions:
                            nr = r + y
                            nc = c + x
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in ('O', '#'):
                                if grid[nr][nc] == '#':
                                    return d + 1
                                q.append((nr, nc, d+1))
                                grid[nr][nc] = 0
        return -1