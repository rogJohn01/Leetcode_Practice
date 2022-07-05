class Solution {
public:
    int trap(vector<int>& h) {
        
         
        int rain = 0 ; 
        int l =1 , r = h.size()-1 ; 
        int maxl = h[0] ,  maxr = h[h.size()-1] ; 
        while( l <=r ) { 

            if( maxl < maxr){ 
                if( h[l] > maxl) maxl = h[l] ; 
                else {
                    rain += maxl-h[l] ; } 
                l++ ; 
            }
            else { 
                if( h[r] > maxr) maxr = h[r] ; 
                else { 
                    rain += maxr - h[r] ; } 
                r -- ;
            }
        }
        return rain ;  
    
        
    }
};