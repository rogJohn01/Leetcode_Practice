class Solution {
    public int findJudge(int n, int[][] trust) {
        
        int[] follower = new int[n+1] ;
        int[] followed = new int[n+1] ;

        for(int[] t:trust){
            follower[t[1]]++ ; 
            followed[t[0]]++ ;
        }
        for(int ix=1 ; ix <=n ; ix++){
            if( follower[ix] ==n-1 && followed[ix] ==0 ){
                return ix ; 
            }
        }
        
        return -1  ; 

    }
}