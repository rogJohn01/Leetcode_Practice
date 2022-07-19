class Solution {
public:
    vector<vector<int>> generate(int nrow) {
        

        vector<vector<int>> tri ; 
        for(int r=0; r < nrow ; r++){
            vector<int> row(r+1,1); 
            for(int c=1; c<r ; c++){
                row[c] = tri[r-1][c] + tri[r-1][c-1] ;
            }
            tri.push_back(row) ; 
        }
        return tri ; 



        
        
    }
};