class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& mat, int target) {
        
        
        int ans = 0 , R = mat.size() , C = mat[0].size() ; 
        for(int r= 0; r < R ; r++)
            for(int c = 1 ; c < C ; c++)
                mat[r][c] += mat[r][c-1] ; 

        unordered_map<int,int> cntr ; 
        for(int y1 =0; y1 < C ; y1++){
            for(int y2= y1 ; y2 < C ; y2++){
                cntr = {{0,1}}; 
                int sv = 0 ; 
                for(int x =0 ; x < R ; x++){
                    sv += mat[x][y2] - ( y1 >0 ? mat[x][y1-1] : 0) ; 
                    ans += cntr.find(sv-target) != cntr.end()? cntr[sv-target] : 0;
                    cntr[sv] ++ ; 
                }}}
        return ans ; 
    }
};