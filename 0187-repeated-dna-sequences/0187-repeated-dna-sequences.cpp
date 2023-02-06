class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        
    
    map<string,int> seen ; 
    vector<string> ans ; 
    if(s.size() <10) return ans ; 
    for(int i=0 ; i <= s.size()-9 ; i++){
        //cout << s.substr(i,10) << "\n" ; 
        seen[s.substr(i,10)] ++ ; 
        if( seen[s.substr(i,10)] ==2  ){
            ans.push_back(s.substr(i,10)) ; 
        }
    }
    return ans; 
        
        
    }
};