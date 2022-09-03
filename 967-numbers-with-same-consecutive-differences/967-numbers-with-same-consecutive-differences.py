class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        
        def backtrack(ix, sd): 
            
            if ix ==n:
                ans.add(sd)
                return 
            
            if ix==0: 
                for i in range(1,10):
                    
                    backtrack(ix+1 , sd+str(i))
            else: 
                t1 = int(sd[-1])+k
                if  t1 <10:
                    backtrack(ix+1, sd+str(t1))
                t2 = int(sd[-1])-k 
                if t2 >=0:
                    backtrack(ix+1 , sd+str(t2))
        
        
         
        ans = set()
        backtrack(0 ,"")
        return ans 