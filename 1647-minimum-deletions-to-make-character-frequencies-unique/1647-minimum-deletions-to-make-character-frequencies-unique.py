class Solution:
    def minDeletions(self, s: str) -> int:
        

        cntr = Counter(s) 

        seen = set() 
        cnt = 0 
        for k ,v in cntr.items(): 

            if v in seen:  
                while v!=0 and v in cntr.values(): 
                    v -=1 
                    cnt +=1 
                cntr[k] = v 
            else: 
                seen.add(v) 

        return cnt 