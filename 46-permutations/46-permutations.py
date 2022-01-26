class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        prev = [] 
        ret = []
        def dfs(elements):
            
            
            if len(prev) == len(nums):
                ret.append(prev[:])
                
                
            for e in elements:
                next = elements[:]
                
                next.remove(e)
                prev.append(e)
                
                dfs(next)
                prev.pop()
                 
        
        dfs(nums)
        return ret 