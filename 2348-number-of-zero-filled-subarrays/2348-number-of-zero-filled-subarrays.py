class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        
        dp = [0]*(10**5+1)
        dp[0] = 0 
        for i in range(1,10**5+1):
            dp[i] = i + dp[i-1]
            
        combo =0 
        ans = 0 
        for n in nums: 
            
            if n ==0: 
                combo +=1 
            else: 
                ans += dp[combo]
                combo =0 
                
        if combo:
            ans += dp[combo]
        
        return ans 
            