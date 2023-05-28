class Solution:
    def differenceOfDistinctValues(self, mat: List[List[int]]) -> List[List[int]]:
        
        


        R = len(mat)
        C = len(mat[0])

        def check(r,c):

            x = r ; y = c 
            x -= 1 ; y -=1 
            topleft = set() 
            while 0<= x < R and 0<= y < C:
                topleft.add(mat[x][y])
                x -=1 ; y -=1 


            x = r ; y = c 
            x += 1 ; y +=1 
            bottomright = set()
            while 0<= x < R and 0<= y < C:
                bottomright.add(mat[x][y])
                x +=1 ; y +=1 


            return  abs(len(topleft) - len(bottomright))


        ans = [ [0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                ans[r][c] = check(r,c)
        
        return ans 


