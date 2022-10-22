class Solution {
public:
    string minWindow(string s, string t) {
         
        unordered_map<char, int> map ;
        for(auto c : t) map[c]++ ; 
        int cnt = 0 ; 
        int low = 0 , mlen = INT_MAX , mstart = 0 ; 
        for(int high = 0 ; high < s.length() ; high ++) { 
                if( map[s[high]]> 0 ) cnt ++ ; 
                map[s[high]]-- ; 
                if(cnt == t.length()){ 
                    while(low < high && map[s[low]] < 0 ){
                        map[s[low]]++ ;
                        low ++;
                    }
                    if( mlen > high-low ) {
                        mlen = high-(mstart = low) +1 ; }
                    map[s[low++]]++ ; 
                    cnt -- ; 
                }
            }
            return mlen == INT_MAX ? "": s.substr(mstart , mlen) ; 
            }
 
    
};