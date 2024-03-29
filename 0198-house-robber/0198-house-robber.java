class Solution {
    
    int[] dp; 
    public int rob(int[] nums) {
        dp = new int[nums.length+1]; 
        Arrays.fill( dp , -1) ; 
        return rob(nums, nums.length -1) ;
    }
    
    private int rob(int[] nums, int i){
        if( i< 0){
            return 0;
        }
        if(dp[i] >= 0){
            return dp[i]; 
        }
        int ans = Math.max( rob(nums, i-2) + nums[i] , rob(nums, i-1)) ;
        dp[i] = ans; 
        return ans; 
        
    }
}