class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        n = len(cost)
        dp = [0]*(n+2)
        def helper(x):
            if x <=0:
                return 0
            if dp[x]:
                return dp[x]
            
            dp[x] = min( helper(x-1), helper(x-2))+ cost[x-1]
            return dp[x]
            
            
        helper(n)
        return dp[-2]
            
            