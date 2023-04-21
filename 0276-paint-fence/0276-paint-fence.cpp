class Solution {
public:
    int dp[51] ;
    int numWays(int x, int k) {
        
        if(x==1) return k ; 
        if(x==2) return k*k ; 

        if(dp[x]) return dp[x] ;

        dp[x] = (k-1)*(numWays(x-1,k)+ numWays(x-2,k)) ; 
        return dp[x] ; 
    }
    

};