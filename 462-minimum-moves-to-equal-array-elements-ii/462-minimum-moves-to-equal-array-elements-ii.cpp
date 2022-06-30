class Solution {
public:
    int minMoves2(vector<int>& nums) {
        
    sort(nums.begin() , nums.end()) ; 
    int ans = 0 , N = nums.size() ; 
    for( int i=0 ; i < N/2 ; i++){
        ans += (nums[N-1-i] -nums[i] ); 
    } 
    
        return ans; 


    }
};