class Solution {
public:
    int R , C ; 
    int memo[50][50][51] ; 
    int dir[5] = {0,1,0,-1,0} ; 
    
    int findPaths(int R, int C, int maxMove, int sx, int sy) {


        this->R = R; this->C = C; 
        memset( memo, -1, sizeof(memo)); 
        return dfs( sx ,sy , maxMove); 
    
}

int dfs(int x,int y , int mleft){ 

    if( x <0 || x ==R || y < 0 || y ==C) return 1; 
    if(!mleft) return 0 ; 

    if(memo[x][y][mleft] != -1) return memo[x][y][mleft] ; 

    int ans = 0 ; 
    for( int i=0 ; i <4 ; i++)
        ans = ( ans + dfs(x+dir[i] ,y+dir[i+1] , mleft-1 )) % 1000000007 ;
    return memo[x][y][mleft] = ans; 
    }

};