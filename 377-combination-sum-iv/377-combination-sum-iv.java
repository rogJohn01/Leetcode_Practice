class Solution {
    public int combinationSum4(int[] nums, int tar) {
        
        
        int[] dp = new int[tar +1 ] ; 
        dp[0] =1 ; 

        for(int tot = 1 ;  tot <= tar ; tot++){
            for(int n:nums){
                if( tot - n >=0){
                    dp[tot] += dp[tot-n] ; 
                }}}
        return dp[tar]  ; 
        
        
    }
}