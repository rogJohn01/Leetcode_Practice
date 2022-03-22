class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        r = len(grid); c =len(grid[0])
        t = r*c 

        ans = [[0]*c for _ in range(r) ]
        for i in range(r*c):
            ans[ ((i+k)%t)//c][((i+k)%t) %c ] = grid[i//c][i%c]
        
        return ans 