class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        cnt = 0
        for i in range(len(nums)):

            if i>0 and nums[i-1] >= nums[i]:
                k = nums[i-1] - nums[i]
                nums[i] += k+1 
                cnt += k+1 
        return cnt