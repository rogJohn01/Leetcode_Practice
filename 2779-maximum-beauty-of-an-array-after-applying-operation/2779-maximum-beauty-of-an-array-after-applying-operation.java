class Solution {
    public int maximumBeauty(int[] nums, int k) {
        
        Arrays.sort(nums) ; 
        int l = 0 ; 
        int r ; 
        for(r=0 ; r < nums.length ; r++){
            if( nums[r]- nums[l] > 2*k){
                l ++ ; 
            }
        }
        return r-l ; 
    }
}