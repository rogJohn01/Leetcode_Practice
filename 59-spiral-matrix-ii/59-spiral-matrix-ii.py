class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [ [0]*n for _ in range(n)]

        dir = [ [0,1] , [1,0] ,[0,-1] ,[-1,0] ]
        x = 0 ; y = 0 
        i =1
        mat[x][y] = i

        while i < n*n:

            for a, b in dir:
                nx , ny = x+a ,y+b 

                while 0<= nx < n and 0<= ny < n and mat[nx][ny] ==0:
                    i +=1 
                    mat[nx][ny] = i 

                    nx +=a
                    ny +=b 
                
                nx -=a
                ny -=b
                x = nx 
                y = ny 

        return mat 