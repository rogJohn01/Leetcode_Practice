class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        d = [0]*(amount+1)
        
        d[0] =1 
        
        for coin in coins:
            for i in range(coin, amount+1):
                d[i] += d[i-coin]
        return d[amount]