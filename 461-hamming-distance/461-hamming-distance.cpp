class Solution {
public:
    int hammingDistance(int x, int y) {
        
        int Xor = ( x ^ y) ; 
        int dist = 0 ; 
        while (Xor) { 
            dist ++ ; 
            Xor = Xor & (Xor-1) ; } 

        return dist ;
        


    }
};