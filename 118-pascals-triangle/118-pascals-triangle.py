class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        tri = [] 
        for n in range(numRows):
            
            row = [None for _ in range(n+1)]
            row[0] , row[-1] = 1 ,1 
            
            
            for j in range(1, len(row)-1):
                
                row[j] = tri[n-1][j-1]+ tri[n-1][j]
            tri.append(row)
        return tri 
            
            