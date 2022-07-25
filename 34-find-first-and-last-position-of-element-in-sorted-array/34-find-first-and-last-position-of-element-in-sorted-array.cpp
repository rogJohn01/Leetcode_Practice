class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int tar) {
        

            int lx = lower_bound( nums.begin() , nums.end() , tar) - nums.begin() ;
            if( lx == nums.size() || nums[lx] != tar) return {-1,-1} ; 
            int hx = upper_bound( nums.begin() ,nums.end() , tar) - nums.begin() -1;    return {lx,hx} ; 


        
        
    }
};