class Solution:
    def cutOffTree(self, mat: List[List[int]]) -> int:
        

        order = [] 
        R = len(mat) ; C = len(mat[0]) 
        for r in range(R):
            for c in range(C):
                if mat[r][c] >=2:
                   order.append( mat[r][c] ) 

        order.sort() 

        def bfs(): 

            visit = set() 
            t = 0 
            i = 0 
            d= 0
            q = deque() 
            q.append([0,0,d])     
            while q: 

                x,y,d = q.popleft() 
                if mat[x][y] == order[i]:
                    if i+1 ==len(order):

                        return t+d 
                    visit = set() 
                    i +=1 
                    t += d 
                    d = 0 
                    mat[x][y] =1 
                    q = deque() 




                for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:  
                    nx, ny =  x+a , y+b 

                    if 	0<= nx < R and 0 <= ny <C: 
                        if (nx,ny) not in visit and mat[nx][ny] !=0:
                            q.append([nx,ny,d+1])
                            visit.add((nx,ny)) 
            return -1 
        return bfs() 




