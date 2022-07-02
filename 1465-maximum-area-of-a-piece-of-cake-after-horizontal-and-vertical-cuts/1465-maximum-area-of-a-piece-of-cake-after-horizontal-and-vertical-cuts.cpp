class Solution {
public:
    int maxArea(int h, int w, vector<int>& hcut, vector<int>& vcut) {
        
        vcut.insert( vcut.begin() , 0) ;
        vcut.push_back(w) ; 
        hcut.insert(hcut.begin() , 0) ; 
        hcut.push_back(h) ; 
        sort(vcut.begin() , vcut.end()) ; 
        sort(hcut.begin() , hcut.end()) ; 
        
        int maxv = 0 , maxh = 0 ; 
        for(auto i=1 ; i<vcut.size() ; i++){
            maxv = max(maxv , vcut[i]-vcut[i-1]) ;
        }
        for(auto j=1 ; j < hcut.size() ; j++){
            maxh = max(maxh , hcut[j]-hcut[j-1]) ; 
        }
        
        return (long)maxh*maxv % 1000000007 ;  
    }
};