class Solution:
    def minSwaps(self, s: str) -> int:
        
        
        res , bal = 0,0 
        for e in s:
            if e=='[':
                bal +=1 
            else:
                bal -=1
            
            if bal ==-1:
                res +=1
                bal = 1
        return res 