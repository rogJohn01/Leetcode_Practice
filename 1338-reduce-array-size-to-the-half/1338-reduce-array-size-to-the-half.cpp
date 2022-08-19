class Solution {
public:
    int minSetSize(vector<int>& arr) {
        
        unordered_map<int,int> mp ; 
        for(auto n:arr){ 
            mp[n]++ ; } 

        vector<int> box ; 
        for(const auto& m:mp){
            box.push_back(m.second) ; } 
        sort(box.begin() , box.end() , greater<int>()); 
        int ans= 0 , tmp = 0 ; 
        for(auto b:box){
            ans ++ ; 
            tmp += b ; 
            if(tmp >= arr.size()/2) return ans ; 
        }
        return ans ; 

    }
};