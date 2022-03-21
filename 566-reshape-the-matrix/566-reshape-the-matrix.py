class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        
        
            m = len(mat) ; n = len(mat[0])
            if r*c != m*n: 
                return mat 

            ans = [[0]*c for _ in range(r) ]

            for i in range(m*n):

                ans[ i//c][i %c] = mat[i//n][i%n]

            return ans 
