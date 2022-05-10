class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        


        nl = len(nums) 
        if nl==0:
            return 0 
        maxfar = nums[0] 
        minfar = nums[0] 
        res = maxfar 

        for i in range(1, nl):
            cur = nums[i] 
            tempMax = max( cur , maxfar*cur , minfar*cur )
            minfar = min( cur , maxfar*cur , minfar*cur) 
            maxfar = tempMax 
            res = max( res , maxfar) 

        return res 