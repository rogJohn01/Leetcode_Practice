class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        
        priority_queue<vector<int> , vector<vector<int>>, Check> q; 
        for(auto bxt :boxTypes){
            q.push(bxt) ; } 
        int uload = 0 ; 
        while(! q.empty()){ 
            int bx  = q.top()[0] ; int un = q.top()[1] ; 
            q.pop() ; 
            int bxload = min(truckSize , bx) ; 
            uload += bxload*un; 
            truckSize -= bxload ; 
            if( truckSize == 0) break ; 
        }
        return uload ; 
    }
        struct Check {
            bool operator()(vector<int> const& p1 , vector<int> const& p2){
                return p1[1] < p2[1] ; 
            }
        };


        
        
    
};