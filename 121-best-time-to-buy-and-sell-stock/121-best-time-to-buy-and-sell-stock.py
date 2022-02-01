class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        


        maxcur  = maxfar  = 0 
        for i in range(1,len(prices)):
            maxcur = max( 0 , maxcur + prices[i]-prices[i-1] )
            maxfar = max( maxcur , maxfar)
        return maxfar 