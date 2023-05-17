class Solution {
    public int maxLength(int[] ribbons, int k) {
        
        int l = 100000;
        int r = 0 ; 
        for(var rib:ribbons){
            l = 0 ;
            r = Math.max(r, rib) ; 
        }
        
        
        while(l<r){
            int m = (l + r + 1) / 2    ;        
            int tot= 0 ; 
            if(m !=0){
                for(var rib:ribbons){
                tot += rib /m ; 
            }
            }
          
            
            if( tot >= k){
                l = m  ;
            }else{
                r = m -1 ;
            }
            
        }
        return r ; 
        
    }
}