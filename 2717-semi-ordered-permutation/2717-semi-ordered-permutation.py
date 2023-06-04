class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        
        cnt =0 
        N = len(nums)
        ix_1 = 0 
        ix_n  = 0 
        for i in range(len(nums)):
            
            if nums[i] ==1: ix_1 = i
            elif nums[i] ==len(nums) : ix_n = i 
                
        
        #print("ix_1: " , ix_1)
        #print("ix_n: " , ix_n )
        cnt += ix_1 
        cnt += (N-1 - ix_n)
        if ix_n < ix_1:
            cnt -=1 
            
            
        return cnt 