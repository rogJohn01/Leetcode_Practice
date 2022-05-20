class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
       
    
        if mat[0][0] ==1:
            return 0 

        R = len(mat) ; C = len(mat[0]) 
        wall = False 
        for r in range(R):
            if mat[r][0] ==1 or wall:
                wall = True 
                mat[r][0] = 0
            else:
                mat[r][0] =1 
        wall = False 
        for c in range(1,C):
            if mat[0][c] ==1 or wall:
                wall = True 
                mat[0][c] = 0 
            else: 
                mat[0][c] = 1 

        for r in range(1,R):
            for c in range(1,C):
                if mat[r][c] == 0:
                    mat[r][c] = mat[r-1][c] + mat[r][c-1] 
                else: # mat[r][c] ==1 
                    mat[r][c] = 0
        return mat[R-1][C-1] 

