class Solution {
public:
    int longestIdealString(string s, int k) {
        
        vector<int> dp(26,0) ; 
        for( int i =0; i < s.size() ; i++){
            int cix = s[i] - 'a'; 
            int ans = 1 ;
            for( int j=0 ; j < 26 ; j++){
                if( abs(j-cix) <=k){
                    ans = max(ans , dp[j]+1); 
                }
            }
            dp[cix] = ans ; 
        }
        return *max_element(dp.begin() , dp.end() ) ; 

    }
};