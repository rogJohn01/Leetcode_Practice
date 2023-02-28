class Solution {
    public int maxSubArray(int[] nums) {
        
        
        int curSubv = nums[0] ; 
        int maxSubv = nums[0] ;
        for(int i=01 ; i < nums.length ; i++){
            
            int n = nums[i] ; 
            curSubv = Math.max(curSubv+n ,  n  ) ; 
            maxSubv = Math.max( curSubv , maxSubv ) ; 
        }
        return maxSubv ; 
        
    }
}