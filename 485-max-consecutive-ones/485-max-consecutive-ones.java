class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        if (nums.length ==1) return nums[0];
        
        int cnt =0 ; 
        int maxv =0 ; 
        for (int i=0; i<nums.length; i++){
            
            if(nums[i]==1){
                cnt ++;
                maxv = Math.max(cnt , maxv);
                
            }
            if( i>=1  && nums[i] ==0 && nums[i-1] ==1){
                cnt =0; 
            }
            
        }
        return maxv;
        
        
    }
}