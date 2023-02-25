class Solution {
    fun maxProfit(prices: IntArray): Int {
        
        if(prices.isEmpty()) return 0 

        var mxProfit = 0 
        var lowprice = prices[0]

        for(price in prices){
            lowprice = kotlin.math.min(lowprice ,price)
            var profit = price - lowprice 
            mxProfit = kotlin.math.max(mxProfit , profit)
        }
        return mxProfit 

    }
}