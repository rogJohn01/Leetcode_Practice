class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        
        sl = len(s)
        pl = len(p)
        
        if pl > sl:
            return 
        
        pCount = [0]*26
        sCount = [0]*26
        
        for e in p:
            pCount[ord(e)-ord('a')] +=1 
        
        ret = [] 
        for i in range(sl):
            
            
            sCount[ord(s[i]) -ord('a')] += 1
            
            if i >=pl:
                sCount[ord(s[i-pl]) -ord('a')]  -=1
                
            if sCount ==pCount:
                ret.append( i-pl+1)
        return ret 
        