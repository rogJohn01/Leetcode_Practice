class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        
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
        box = [] 
        for ans in ret:
            
            if ans not in box:
                box.append(ans)
        return box 