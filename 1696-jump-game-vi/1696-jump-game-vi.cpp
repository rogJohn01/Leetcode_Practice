class Solution {
public:
    int maxResult(vector<int>& nums, int k) {
        
        

        int N = nums.size() ; 
        vector<int> dp(N) ; 
        dp[0]= nums[0] ; 
        deque<int> q ; 
        q.push_back(0); 

        for( int i=1; i < N ; i++){

            while( !q.empty() && q.front() < i-k){
                q.pop_front() ; } 

            dp[i] = dp[q.front()] + nums[i] ; 

            while( !q.empty() &&  dp[i] >= dp[q.back()] ){
                q.pop_back() ; } 

            q.push_back(i) ;  
        }
        return dp[N-1] ; 


        
        
        
        
    }
};