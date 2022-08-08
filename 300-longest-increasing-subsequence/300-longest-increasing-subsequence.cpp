class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
         
    vector<int> sub ; 
    for(auto n:nums){
        auto ix = lower_bound(sub.begin() , sub.end() , n) ;

        if (ix == sub.end())
            sub.push_back(n) ; 

        else *ix = n  ;  

    }
    return  sub.size() ; 
    
        
        
    }
};