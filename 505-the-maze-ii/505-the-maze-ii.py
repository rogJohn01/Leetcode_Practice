class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n , q = len(maze) , len(maze[0]) , [(0,start[0],start[1])]
        stopped = {(start[0], start[1]):0}

        while q: 
            dist , x, y = heapq.heappop(q)
            if [x,y] == destination:
                return dist 
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx , ny , d = x, y, 0 
                while 0<= nx+a <m and 0<=ny+b < n and maze[nx+a][ny+b] !=1:
                    nx +=a
                    ny +=b 
                    d+=1 
                if (nx,ny) not in stopped or dist+d < stopped[(nx,ny)]:
                    stopped[(nx,ny)] = dist+d
                    heapq.heappush(q, (dist+d, nx ,ny))
        return -1 