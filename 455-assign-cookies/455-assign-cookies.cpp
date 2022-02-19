class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        
        sort(g.begin(), g.end());
        sort(s.begin() , s.end()); 
        int cnt = 0;
        int k =0;
        for(int s1:s){
            
            if( k == g.size()) break; 
            
            if (s1 >= g[k] ){
                ++cnt;
                ++k; 
            }
            
        }
        return cnt;
        
        
        
    }
};