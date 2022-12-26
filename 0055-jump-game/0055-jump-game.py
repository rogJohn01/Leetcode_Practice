class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        ln = len(nums)
        dp = [0]*ln 
        dp[0] = nums[0] 
        if ln ==1:
            return True 
        
        for i in range(1, ln-1):
            
            if dp[i-1] < i:
                return False 
            
            dp[i] = max( i+nums[i] , dp[i-1] )

            if dp[i] >= ln-1:
                return True 
        
        return  dp[ln-2] >= ln-1 

