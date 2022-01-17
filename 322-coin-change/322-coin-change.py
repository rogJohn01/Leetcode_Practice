class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        d = [float('inf')]*(amount+1)
        
        d[0] = 0
        
        
        for coin in coins:
            for x in range(coin,amount+1):
                
                d[x] = min(d[x], d[x-coin]+1)
        return d[amount] if d[amount] !=float('inf') else -1 