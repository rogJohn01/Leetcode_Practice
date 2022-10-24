class Solution {
public:
    int maxLength(vector<string>& arr) {
        
    vector<bitset<26>> dp = {bitset<26>()};
    int ans = 0;
    for(auto& s: arr){
        bitset<26> bit ; 
        for(char c : s){
            bit.set(c-'a'); }
        int n = bit.count(); 
        if( n < s.size()) continue ; 

        for( int i= dp.size() -1 ; i>= 0 ; --i){
            bitset bit2 = dp[i] ;
            if ((bit2 & bit).any()) continue ; 
            dp.push_back(bit2|bit) ;
            ans = max(ans, (int)bit2.count()+n);
        }
    }
    return ans; 
    }
};