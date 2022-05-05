class Solution:
    def shortestPathBinaryMatrix(self, mat: List[List[int]]) -> int:
        if mat[0][0] ==1:
            return -1 
        
        
        q = deque()
        q.append([0,0,1] ) 
        R = len(mat) ; C = len(mat[0]) 
        cnt = 0 
        visit = set() 
        while q:

            x, y ,t= q.popleft() 

            if [x,y] == [R-1,C-1]:
                return t  

            for a,b in [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,-1),(-1,1),(1,1)]:
                nx, ny =  x+a , y+b 

                if 0<=nx < R and 0 <= ny <C:
                    if mat[nx][ny] ==0 and (nx,ny) not in visit:  
                        q.append([nx,ny,t+1 ] )  
                        visit.add((nx,ny) ) 

        return -1

