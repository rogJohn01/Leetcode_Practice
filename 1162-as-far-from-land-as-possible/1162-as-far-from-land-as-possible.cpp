class Solution {
public:
    int maxDistance(vector<vector<int>>& grid) {
    
    int dx[] = {-1,0,1,0};   
    int dy[] = {0,1,0,-1};

    int R = grid.size() ;
    int C = grid[0].size() ;

    queue<pair<int,int>> q; 

    for(int r=0 ; r<R ; r++){
        for(int c=0; c<C ; c++){
            if(grid[r][c]==1){
                q.push({r,c}) ; 
            }
        }
    }

    if(q.size()==R*C) return -1 ; 

    int dis =0 ; 

    while(q.size()){
        int sz = q.size(); 
        dis ++ ; 
        while(sz--){
            auto [sx,sy] = q.front() ; 
            q.pop() ; 
            for(int i=0 ; i< 4; i++){

                int nx = sx+dx[i] ; 
                int ny = sy+dy[i] ; 
                if(0<=nx && nx < R && 0<= ny && C ){
                    if(grid[nx][ny] == 0){
                        q.push({nx,ny}) ; 
                        grid[nx][ny] =1 ; 
                    }
                }
            }
        }
    }
    return dis-1 ; 


    }
};