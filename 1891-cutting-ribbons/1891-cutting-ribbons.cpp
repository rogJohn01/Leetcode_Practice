class Solution {
public:
    int maxLength(vector<int>& ribbons, int k) {
     
        int cnt ; 
        int l = 1; 
        int r = *max_element(ribbons.begin() , ribbons.end()) ;
        

        while(l<=r){

            int m = l+ (r-l)/2 ; 
            cnt = 0 ; 
            for(auto r:ribbons){
                cnt +=  r/m  ;
            }

            if(cnt < k){
                r = m-1; 
            }else {
                l = m+1; 
            }
           

        }return r ; 
    }
};