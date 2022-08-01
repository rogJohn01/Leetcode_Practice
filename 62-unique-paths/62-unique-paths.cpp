class Solution {
public:
    int uniquePaths(int R, int C) {
        
        
        vector<int> cdp(C ,1);
        for(int r =1; r < R ; r++){
            for(int c =1 ; c < C ; c++){ 
                cdp[c] += cdp[c-1] ; 
            }}
        return cdp[C-1] ; 



        
       
        
    }
};