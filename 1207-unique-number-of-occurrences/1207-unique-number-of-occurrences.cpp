class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        unordered_map<int,int> map ; 
        for(auto a:arr){
            map[a]++ ; 
        }
        unordered_set<int> mset; 
        for(auto& kv : map){
            if( mset.count(kv.second)){
                return false; 
            } else {
                mset.insert(kv.second) ; 
            }
        }
        return true ; 
        
        
    }
};