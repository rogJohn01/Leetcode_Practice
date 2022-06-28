class Solution {
public:
    int minDeletions(string s) {
        
    vector<int> fq (26 ,0) ; 
    for(auto e:s){ 
        fq[e-'a'] ++  ; } 
    sort(fq.begin() , fq.end()) ; 
    int ans = 0 ;
    for(int i=24 ; i >=0 ; i--){ 
        if( fq[i] ==0) break ; 
        
        if(fq[i] >=fq[i+1]) {
                int prv = fq[i] ; 
                fq[i] = max(0, fq[i+1] -1) ; 
                ans += prv - fq[i] ; 
                }
            }
        return ans ; 


        
        
    }
};