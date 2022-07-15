class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& mat) {
        int ans = 0 ; 
        int R = mat.size() , C = mat[0].size() ; 

        for(int r=0 ; r<R ; r++){
            for(int c=0 ; c<C ; c++){ 
                if( mat[r][c] ==1 ){ 
                    ans = max(ans, dfs(r,c, mat)) ;;  
        }}}
        return ans ; 
    }

    int dfs(int x,int y, vector<vector<int>>& mat){ 
        int R = mat.size() , C = mat[0].size() ; 
        vector<vector<int>> dir {{1,0},{-1,0},{0,1},{0,-1}} ; 
        mat[x][y] = 0 ; 
        int cnt = 1; 
        for(auto d:dir){ 
            int nx = x+d[0] , ny = y+d[1] ; 
            if(0<=nx && nx< R && 0<=ny && ny<C)
                if(mat[nx][ny] ==1)
                    cnt +=  dfs(nx,ny ,mat ) ; } 
        return cnt ;
    }

};