class Solution:
    def combinationSum4(self, nums: List[int], tar: int) -> int:
        
        
        @lru_cache(maxsize = None )
        def dfs(rem):
            
            if rem ==0: return 1 
            
            res = 0 
            for n in nums: 
                if rem - n >=0: 
                    res += dfs(rem-n)
            
            return res 
        
        return dfs(tar)