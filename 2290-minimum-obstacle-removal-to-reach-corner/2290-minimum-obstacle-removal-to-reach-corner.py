class Solution:
    def minimumObstacles(self, mat: List[List[int]]) -> int:
        import heapq as hq 
        inf = float('inf') 
        R = len(mat) ; C = len(mat[0]) 
        dist = [[inf]*C for _ in range(R) ] 
        hp = [ ( mat[0][0] , 0, 0 ) ] 
        dist[0][0] = mat[0][0] 

        while hp: 

            w , x, y = hq.heappop(hp)
            if [x,y] == [R-1,C-1]:
                return w 
            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:  
                nx, ny =  x+a , y+b 
                if 	0<= nx < R and 0 <= ny <C: 
                    if mat[nx][ny] + w < dist[nx][ny]: 
                        dist[nx][ny] = mat[nx][ny] + w 
                        hq.heappush(hp , (dist[nx][ny] , nx,ny ))


