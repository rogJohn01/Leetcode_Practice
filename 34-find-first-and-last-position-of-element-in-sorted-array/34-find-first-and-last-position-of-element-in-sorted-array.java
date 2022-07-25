class Solution {
    public int[] searchRange(int[] nums, int tar) {
        
        
        int sx = Solution.bs(nums ,tar) ; 
        if( sx == nums.length || nums[sx] !=tar) return new int[]{-1,-1} ;
        return new int[]{sx ,Solution.bs(nums,tar+1) -1} ; 
    }
    private static int bs(int[] nums, int tar){ 
    
        int l =0 , h = nums.length ; 
        while(l < h ){
            int m = l+((h-l)>>1) ;

            if(nums[m] < tar) l = m+1 ;
            else h = m ; 
        }
        return l ; 
  
    }
}