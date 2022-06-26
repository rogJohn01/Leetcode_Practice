class Solution {
public:
    int numJewelsInStones(string j, string S) {
        
        
        int ans =0 ; 
        unordered_set<char> setJ(j.begin() , j.end()) ;
        for(auto s:S){
            if(setJ.count(s))  ans ++; }
        
        return ans ; 
        
        
        }
        
        
};