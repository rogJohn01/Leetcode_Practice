class Solution:
    def searchMatrix(self, matrix: List[List[int]], tar: int) -> bool:
        
        for row in matrix: 
            ix = bisect.bisect_left(row, tar)
            if ix >=len(row): continue 
            if row[ix] == tar: return True 
        return False  
            