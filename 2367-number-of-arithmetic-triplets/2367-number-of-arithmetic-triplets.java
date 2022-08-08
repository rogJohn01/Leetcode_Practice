class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        
        
        Set<Integer> hash = new HashSet<>(); 
        int ans = 0 ; 
        for(int n:nums){
            if(hash.contains(n-diff) && hash.contains(n-2*diff)) ans ++ ;
        
        hash.add(n) ;
        }
        return ans ; 
        
    }
}