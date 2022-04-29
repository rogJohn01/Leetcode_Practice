class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       
        

        nl = len(nums) 
        dp = [1]*nl 
        for i in range(1,nl):
            for j in range(i): 
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i] , dp[j] +1 )

        return max(dp)