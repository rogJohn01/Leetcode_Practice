class Solution:
    def maxSubArray(self, nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        print(dp)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)