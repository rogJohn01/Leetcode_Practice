class Solution:
    def numSubmatrixSumTarget(self, mat: List[List[int]], target: int) -> int:
         
        R = len(mat) ; C = len(mat[0]) 
        for r in range(R):
            for c in range(C-1):
                 mat[r][c+1] += mat[r][c] 

        ans = 0 
        for y1 in range(C):
            for y2 in range(y1,C): 
                prSum = {0:1} 
                sv = 0 
                for x in range(R): 
                    sv += mat[x][y2] - (mat[x][y1-1] if y1>=1 else 0 ) 
                    ans += prSum.get(sv-target , 0) 
                    prSum[sv] = prSum.get(sv,0) +1 

        return ans 

