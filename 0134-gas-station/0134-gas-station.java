class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        
        int gl = gas.length ;
        int tsur =0; 
        int sur = 0 ; 
        int start = 0; 
        
        for(int i=0; i<gl;i++){
            tsur += gas[i] - cost[i] ; 
            sur += gas[i] - cost[i] ; 
            if(sur <0){
                sur = 0; 
                start = i+1 ; 
            }
        }
        return (tsur < 0) ? -1:start ; 
    
    }
    
    
}