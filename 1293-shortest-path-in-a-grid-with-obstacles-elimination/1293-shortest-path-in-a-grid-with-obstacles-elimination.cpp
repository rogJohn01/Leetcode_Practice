class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        
        
    int R = grid.size(); 
    int C = grid[0].size(); 

    vector<vector<int>> visit(R , vector<int>(C , -1)); 
    queue<vector<int>> q ; 

    q.push({0,0,0,k}) ; 
    while( !q.empty()){ 
        auto sp = q.front(); 
        q.pop(); 

        int x = sp[0] , y = sp[1] ; 
        if( x < 0 || x >= R || y < 0 || y >= C ) 
            continue ; 
        if( x == R-1 && y == C-1 ) 
            return sp[2] ; 
        if(grid[x][y] ==1 ) {
            if(sp[3] > 0 )
                sp[3] -- ; 
            else 
                continue ; 
        }
        if(visit[x][y] != -1 && visit[x][y] >= sp[3] ) 
            continue ; 

        visit[x][y] = sp[3] ; 

        q.push({x+1 , y , sp[2]+1 , sp[3]}); 
        q.push({x-1 , y , sp[2]+1 , sp[3]}); 
        q.push({x , y+1 , sp[2]+1 , sp[3]}); 
        q.push({x , y-1 , sp[2]+1 , sp[3]}); 
    }
    return -1; 

    }
};