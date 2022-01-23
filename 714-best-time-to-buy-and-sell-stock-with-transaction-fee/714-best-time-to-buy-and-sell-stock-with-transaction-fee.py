class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
        # dush! I need to get the maxium profit!! 
        # maybe dp like coin change? 
        
        # two pointer doesn't work here :( 
        
        # maybe kadane algorithm ? 
        
        
        n = len(prices)
        if n<2: return 0 
        
        ans =0 
        minv = prices[0]
        
        for i in range(1,n):
            if prices[i] < minv:
                minv = prices[i]
            elif prices[i] > minv+fee:
                ans += prices[i] - fee -minv 
                minv = prices[i] - fee
        return ans 