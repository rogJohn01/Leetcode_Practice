class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        
        int cnt = 0 ; 
        for(int i=1 ; i < nums.size() ; i++){
            if( nums[i-1]> nums[i]){
                cnt ++ ; 
                if(i-1 ==0){
                    nums[i-1] = nums[i] ;
                }
                else {
                    if(i>=2 && nums[i-2] <= nums[i]){
                        nums[i-2] = nums[i-1] ; 
                    }
                    else { 
                nums[i] = nums[i-1] ; } 
                }
                if( cnt >1){
                    return false ; 
                }
            }
        }
        return true ; 
        
    }
};