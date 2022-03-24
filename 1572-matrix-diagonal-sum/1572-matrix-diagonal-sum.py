class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        cnt = 0 
        left =0 ; right = len(mat[0])-1 
        while left <n and right > 0:
                
            for row in mat: 
                cnt += row[left]
                cnt += row[right]
                left +=1 
                right -=1 
        
        if n&1 ==1 and n!=1:
            cnt -= mat[n//2][n//2]
        if n==1:
            return mat[0][0]

        return cnt 