class Solution {
public:
    int mySqrt(int x) {
        
        long long start= 0 , end = x , ans , mid;
        
        while( start <=end){
            mid = (start+end)/2;
            if (mid*mid==x) return mid;
            
            else if(mid*mid > x){
               if( (mid-1)*(mid-1) <x ){
                   return mid-1;
               }
               end = mid-1;       
            }  
            else start = mid+1;
        }
        return ans; 
    }
};