class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        
        
        
        int l = 1 , r = *max_element(piles.begin() , piles.end() ) ; 
        while(l<r){
            int m = (l+r) /2 ; 
            

            int sumv = 0 ; 
            for(int p:piles){
                sumv += p/m ; 
                if( p % m != 0) sumv ++ ; 
            }
            
            if(sumv > h){
                l = m+1 ;
            }else {
                r = m  ;
            }
            

        }
        return l ; 
        
        
        
        
    }
};