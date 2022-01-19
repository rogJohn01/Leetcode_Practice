class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        
        leftend , rightend = len(s) , len(t)
        pleft = 0
        pright =0 
        
        while pleft < leftend and pright < rightend:
            
               if s[pleft] == t[pright]:
                  pleft +=1
            
               pright +=1 
        
        
        return pleft == leftend 