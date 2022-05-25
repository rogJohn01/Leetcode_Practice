class Solution {
public:
    int minSteps(string s, string t) {
        
        int cnt =0; 
        vector<int> arr(26,0);

        for(auto e:s) {
            arr[e-'a']++ ; } 

        for(auto e:t){
            arr[e-'a']-- ; } 

        for(auto e:arr){ 
            cnt += abs(e) ; } 

        return cnt ; 

        
        
    }
};