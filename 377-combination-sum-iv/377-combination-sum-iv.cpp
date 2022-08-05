class Solution {
public:
    int combinationSum4(vector<int>& nums, int tar) {
        vector<int> dp(tar+1 , -1) ;
        return dfs(nums , tar , dp) ; 
    }
    

    int dfs(vector<int>& nums , int tar , vector<int>& dp){

        if(tar ==0) return 1 ; 
        if( dp[tar] != -1) return dp[tar] ; 

        dp[tar] = 0 ; 

        for(auto n:nums){
            if( tar- n >=0){
                dp[tar] +=  dfs(nums, tar-n , dp); 
            }}
        return dp[tar ] ; 
    }


    
};