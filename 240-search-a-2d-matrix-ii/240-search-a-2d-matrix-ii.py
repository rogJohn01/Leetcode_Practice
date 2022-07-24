class Solution:
    def searchMatrix(self, matrix: List[List[int]], tar: int) -> bool:
        
        import bisect as bi 
        for row in matrix: 
            ix = bi.bisect_left(row, tar)
            if ix >=len(row): continue 
            if row[ix] == tar: return True 
        return False  
            