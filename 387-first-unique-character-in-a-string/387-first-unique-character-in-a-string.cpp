class Solution {
public:
    int firstUniqChar(string s) {
        
        
        unordered_map<char,int> mp ; 
        for(int i=0; i < s.size() ; i++){
            auto e = s[i] ;  
            if( !mp.empty() &&  mp.find(e) != mp.end())
                mp[e] = 100001 ; 
            else mp[e] = i ; 
        }
        vector<int> values ; 
        for(auto const& m:mp){
            values.push_back( m.second ) ; }

        int minv= *min_element(values.begin() , values.end()) ; 
        return  minv != 100001 ?  minv:-1  ; 
        
        
    }
};