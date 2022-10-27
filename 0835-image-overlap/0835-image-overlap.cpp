class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        
        
        int n = img1.size() ;
        vector<pair<int,int>> vec1 ;
        vector<pair<int,int>> vec2 ; 
        for(int r=0 ; r < n; r++ ) { 
            for( int c=0; c < n ; c++ ){ 
                if( img1[r][c] ==1 ) { 
                    vec1.push_back({r,c}); 
                }
                if( img2[r][c] ==1) { 
                    vec2.push_back({r,c}) ; 
                }
            }
        }
        int ans = 0; 
        map<pair<int,int>, int> box; 
        for(auto [r1,c1] : vec1){
            for(auto [r2,c2] : vec2) { 
                    box[{r1-r2, c1-c2 }]++; 
                    ans = max( ans , box[{r1-r2 , c1-c2}]); 
                    }
                }
        return ans;

        }
};