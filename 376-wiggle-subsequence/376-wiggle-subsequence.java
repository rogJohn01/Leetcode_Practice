class Solution {
    public int wiggleMaxLength(int[] nums) {
        
        int N = nums.length ; 
        if( N==1) return 1 ; 
        
        int up =1 , down = 1 ; 
        for(int i=1 ; i <N ; i++){
            if( nums[i] > nums[i-1]) {
                up = down +1 ; 
            }
            else if ( nums[i] < nums[i-1]){
                down = up +1 ; 
            }
        }
            return Math.max(up,down ) ; 
        
        
        
        
    }
}