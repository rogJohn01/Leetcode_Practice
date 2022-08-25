class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        
        mcntr = Counter(magazine) 

        for e in ransomNote: 
            if mcntr[e] ==0:
                return False 
            mcntr[e] -=1 
        return True 


    
