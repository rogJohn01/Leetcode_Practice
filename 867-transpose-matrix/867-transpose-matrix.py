class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        m = len(mat) ; n = len(mat[0])
        r = n ; c = m 
        ans = [ [0]*c for _ in range(r)]
        for i in range(m*n):
            ans[ i %n  ][i//n] = mat[i//n][i%n] 
            
        return ans 
