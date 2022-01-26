class Solution:
    def isUgly(self, n: int) -> bool:
        
        
        
        for div in [2,3,5]:
            
            while n % div ==0 and 0 < n:
                
                n /= div 
        
        return n==1 
        