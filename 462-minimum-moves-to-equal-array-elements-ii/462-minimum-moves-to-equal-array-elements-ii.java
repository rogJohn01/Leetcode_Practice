class Solution {
    public int minMoves2(int[] nums) {
        int sum = 0; 
        Arrays.sort(nums); 
        for(int n:nums){
            sum += Math.abs(nums[nums.length/2] - n ) ;}
        
        return sum ; 
    }
}