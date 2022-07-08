class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        

        dp = {} 
        inf = float('inf') 

        def helper(i,t,c):
            key = (i,t,c) 

            if i==len(houses) or t < 0 or m-i<t: 
                return 0 if t ==0 and i == len(houses) else inf  

            if key not in dp:
                if houses[i] ==0:
                    dp[key] = min(helper(i+1, t-(nc!=c) , nc) + cost[i][nc-1] for nc in range(1,n+1)) 

                else: 
                    dp[key] = helper(i+1 , t-(houses[i] !=c) , houses[i])

            return dp[key] 

        ans = helper(0,target , -1) 

        return ans if ans < inf else -1 