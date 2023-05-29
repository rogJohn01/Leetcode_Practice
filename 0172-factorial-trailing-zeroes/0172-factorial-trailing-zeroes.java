class Solution {
    public int trailingZeroes(int n) {
        
        int ans = 0 ; 
        while(n != 0){
            int tmp = n/5 ; 
            ans +=tmp ; 
            n = tmp;
        }
        return ans ; 
    }
}