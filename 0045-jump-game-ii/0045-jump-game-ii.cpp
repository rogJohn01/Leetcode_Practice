class Solution {
public:
    int jump(vector<int>& nums) {
        

        int nl = nums.size() ; 
        vector<int> dp(nl,INT_MAX ) ; 
        dp[0] = 0 ; 

        for(int i= 0 ; i < nl ; i++){
            for(int j=0 ; j <= nums[i] ; j++){
                if(j >=1 && i+j < nl ){
                    dp[i+j] = min(dp[i+j], dp[i]+1) ; 
                }
            }
        }
      
        return dp.back() ; 
    }
};