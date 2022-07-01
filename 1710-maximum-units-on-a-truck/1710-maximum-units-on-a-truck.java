class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        
        

        int[] buk = new int[1001] ; 
        for(int[] bx: boxTypes){
            buk[bx[1]] += bx[0] ; } 

        int bxload = 0; 
        for(int ut =1000 ; ut > 0 ; ut--){
            if( buk[ut] > 0 ) { 
                int dif = Math.min( buk[ut] , truckSize ) ; 
                bxload += ut*dif ; 
                truckSize -= dif ; 
                if(truckSize <=0){ 
                    return bxload ; 
                }
            }
        }
        return bxload ; 
    }}

        
        
    
