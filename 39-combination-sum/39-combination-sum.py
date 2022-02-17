class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        
        
        
        
        ret = [] 
        def backtrack(rem , path , start):
            
            
            if rem ==0:
                ret.append(list(path))
                return 
            
            elif rem < 0:
                return 
            
            for i in range(start, len(cand)):
                
                backtrack(rem - cand[i] , path+[cand[i]] , i )
                
        
        backtrack(target , [], 0)
        return ret 