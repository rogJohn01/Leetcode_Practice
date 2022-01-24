class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0 or x==1:
            return x
        for n in range(1, x):
            
             if n*n == x:
                return n 
             if (n+1)*(n+1) >x:
                    return n 