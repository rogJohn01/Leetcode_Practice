class Solution:
    def jump(self, nums: List[int]) -> int:

        nl = len(nums)
        dp = [0]*(nl) 

        for c in range(nl-1): 
            for i in range(1, nums[c]+1):
                if c+i <=(nl-1):
                    if dp[c+i] !=0:
                        dp[c+i] = min(dp[c+i],dp[c]+1)
                    else:
                        dp[c+i] = dp[c] +1 
        return dp[-1] 
