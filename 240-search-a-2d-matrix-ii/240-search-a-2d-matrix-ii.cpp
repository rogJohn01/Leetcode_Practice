class Solution {
public:
    bool searchMatrix(vector<vector<int>>& mat, int tar) {
        
        int R = mat.size() , C = mat[0].size() ; 
        int r = 0 , c = C-1 ; 
        while(r < R && c>=0 ) {
            if(mat[r][c] == tar) return true ; 
            mat[r][c] > tar? c--:r++ ; 
        }
        return false ; 
        
    }
};