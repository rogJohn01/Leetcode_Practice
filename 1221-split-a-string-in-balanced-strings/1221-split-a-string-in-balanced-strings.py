class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        
        cnt , ans = 0,0 
        for e in s:
            
            if e=='L':
                cnt +=1 
            elif e == 'R':
                cnt -=1 
                
            if cnt ==0: 
                ans +=1 
        return ans 
                
        