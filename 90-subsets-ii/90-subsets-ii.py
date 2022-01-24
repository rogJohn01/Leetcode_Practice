class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
     
        ret = [] 
        def dfs(nums,path ,ret):
            
            ret.append(path)
            
            for i in range(len(nums)):
                
                if i>0 and nums[i] == nums[i-1]:
                    continue 
                
                dfs(nums[i+1:],path+[nums[i]],ret )
    
    
    
    
    
    
        dfs(sorted(nums),[] ,ret)
        return ret 