class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        
        int curx = nums[0] ;
        int maxv = nums[0] ; 
        for(int i=1 ; i < nums.size() ; i++){
            int n = nums[i] ;
            curx = max(curx+n , n) ; 
            maxv = max(curx , maxv) ;
            
        }
        return maxv ;
    }
};