class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
            
        cand.sort()
        ret = [] 
        self.backtrack( cand , [] , ret , target , 0)
        return ret 
    
    
    def backtrack(self, nums , path , ret , target ,start):
        
        if not target:
            ret.append(path)
            return 
        
        for i in range(start , len(nums)):
            
            if i > start and nums[i] ==nums[i-1]:
                continue 
            if nums[i] > target:
                break 
            
            self.backtrack(nums,path+[nums[i]] , ret , target - nums[i] , i+1 )