class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        
        
      
        long long al = nums.size() ;
        if(al==1){
            return 0 ;
        }

        vector<long long> prefx1(al , 0 );
        for(long long i=0; i < al ; i++){
            prefx1[i] = nums[i] ; }

        for(long long i=0; i < al-1 ; i++ ) {
            prefx1[i+1] += prefx1[i] ; }
        // backwards

        vector<long long>prefx2 ;
        for(auto n:nums){
            prefx2.push_back(n) ; }

        for(long long i =al-1; i > 0 ; i--){
            prefx2[i-1] += prefx2[i] ; }

        long long ansix , avg2 ;
        long long minv , ans = INT_MAX ;
        for(long long i=0 ; i < al ; i++){

            long long avg1 = ( prefx1[i] > 0 ) ? prefx1[i] /(i+1) : 0 ;
            long long ix = i+1 ;
            if( ix < al ){
            avg2 = ( prefx2[ix] > 0 ) ? prefx2[ix]/(al-(ix))   : 0 ;          } else {
             avg2 = 0 ;
            }

             minv = abs( avg1 -avg2) ;
             if(minv < ans){
                 ans = minv ;
                 ansix = i ;
             }


        }
        return ansix ;

    }
};