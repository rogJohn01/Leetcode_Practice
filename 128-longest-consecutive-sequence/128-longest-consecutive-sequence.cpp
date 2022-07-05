class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        
    unordered_set<int> smap(nums.begin() , nums.end()); 
    int ans = 0 ;
    for(auto n:smap){
        int tmp =1; 
        for(int j=1; smap.count(n-j) ; j++) {
            smap.erase(n-j) ;
            tmp ++  ;  } 
        for(int j=1 ; smap.count(n+j) ; j++){
            smap.erase(n+j) ;
            tmp ++ ; }
        ans = max(ans ,tmp) ; 
    }
    return ans ;  


        
        
    }
};