class Solution {
    public int findPaths(int R, int C, int maxMove, int sx, int sy) {
    
        


        int mod = 1000000007; 
        int[][] memo = new int[R][C] ; 
        memo[sx][sy] =1 ; 
        int ans = 0 ; 

        int[][] dirs =  {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for(int step=0 ; step< maxMove ; step++){
            int[][] tmp = new int[R][C] ; 
            for(int r=0; r <R ; r++)
                for(int c=0; c <C ; c++)
                    for(int[] d:dirs){
                        int nr = r+d[0]  , nc = c+d[1] ; 
                        if( nr <0 || nr>=R || nc <0 || nc >=C )
                            ans = (ans+ memo[r][c] ) % mod ; 
                        else {
                            tmp[nr][nc] = ( tmp[nr][nc] + memo[r][c] )%mod ; 
                        }}
            memo = tmp ;
        }
        return ans ; 



        
        
    }
}