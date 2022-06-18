class Solution:
    def minimumObstacles(self, mat: List[List[int]]) -> int:
        
        R = len(mat) ; C = len(mat[0])
        visit =set()
        visit.add((0,0))
        q = deque()
        q.append([0,0, 0] )
        minv = float('inf')
        while q:
            for _ in range(len(q)):
                x,y, w = q.popleft()

                if [x,y] == [R-1,C-1]:
                    if w < minv:
                        minv = w

                tmp= []
                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny =  x+a , y+b
                    if 	0<= nx < R and 0 <= ny <C:
                        if (nx,ny) not in visit:
                            if mat[nx][ny] ==1:
                                q.append([nx,ny,w+1])
                            else:
                                q.appendleft([nx,ny, w] )
                            visit.add((nx,ny))

        return minv

