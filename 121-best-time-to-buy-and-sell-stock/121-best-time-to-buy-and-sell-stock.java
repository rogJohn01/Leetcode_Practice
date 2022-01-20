class Solution {
    public int maxProfit(int[] prices) {
        
  
        
        int maxcur = 0 , maxsofar = 0;
        for (int i =1 ; i <prices.length ; i++){
            
            maxcur = Math.max(0, maxcur += prices[i]-prices[i-1]);      
            maxsofar = Math.max(maxcur , maxsofar);
            
        }
        return maxsofar;
        
    }
    
}