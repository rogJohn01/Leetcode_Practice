class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
       
        mat = []
        for row in matrix:
            mat +=row
        left = 0 ; right =len(mat)-1

        while left < right:
            
            mid = (left+right) >>1 
            
            if mat[mid] ==target:
                return True 
            
            if mat[mid] > target:
                right = mid -1 
            
            else: 
                left = mid +1 
        
        return True if mat[left] ==target  else False  