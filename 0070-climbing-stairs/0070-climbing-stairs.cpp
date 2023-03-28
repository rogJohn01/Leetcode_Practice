class Solution {
public:
    int dp[47] ; 
    
    int climbStairs(int n) {
        
     memset(dp, -1 ,sizeof(dp)) ;  
     return dfs(n+1) ; 

        
    }
    int dfs(int x){

        if(x==1 ) return 1 ;
        if(x < 0) return 0 ;

        if( dp[x] != -1 ) return dp[x] ; 


        dp[x] = dfs(x-1)+dfs(x-2) ;
        return dp[x] ; 

    }


};