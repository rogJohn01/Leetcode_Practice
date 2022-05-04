class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cl = len(cost)
        dp= [0]*(cl+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        print(cl )     
        print(cost) 
        for i in range(2,cl+1):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])      
        return dp[cl]