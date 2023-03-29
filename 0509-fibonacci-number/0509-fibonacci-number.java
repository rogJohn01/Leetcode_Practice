class Solution {
    
    int[] dp = new int[31] ;  

    public int fib(int n) {
    
        Arrays.fill(dp, -1) ;     
        return dfs(n) ; 
        
    }
    public int dfs(int x){
        if(x==1){
            return 1; 
        }
        if(x==0){
            return 0; 
        }
        if(dp[x] !=-1) return dp[x]; 
        
        dp[x] = dfs(x-1)+dfs(x-2) ;
        return dp[x] ; 
    }
}