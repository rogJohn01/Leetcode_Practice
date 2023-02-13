class Solution {
public:
    
    bool ifeven(int x){
        if(x % 2==0){
            return true ;
        }return false ; 
    }
    
    
    int countOdds(int low, int high) {
        
        if( ifeven(low) && ifeven(high))
            return (high-low)/2 ; 
        
        if( ifeven(low) || ifeven(high))
            return (high-low)/2 +1 ; 
        
        if( !ifeven(low) && !ifeven(high))
             return (high-low)/2 +1 ; 
        
        return 0 ; 
        }
};