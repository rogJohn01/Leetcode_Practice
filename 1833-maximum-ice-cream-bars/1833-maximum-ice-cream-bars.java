class Solution {
    public int maxIceCream(int[] costs, int coins) {
        
        Arrays.sort(costs) ; 
        int ix = 0 ; 

        while( ix < costs.length && costs[ix] <= coins ){
            coins -= costs[ix] ;
            ix ++ ; 
        }
        return ix ; 

    }
}