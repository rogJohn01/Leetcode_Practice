class Solution {
    fun maxProfit(prices: IntArray): Int {
        
        var ans =0  
        for(i in 1 until prices.size ){
            if(prices[i] - prices[i-1] >0){
                ans += prices[i] - prices[i-1]
            }
            
        }
        return ans 
    
        
    }
}