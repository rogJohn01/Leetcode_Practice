class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        
        
    vector<int> ans(2*n,0) ;


    for(int i=0 ; i < 2*n ; i++){

        if(i < n ){
           int  t = i*2 ;
            ans[t] = nums[i] ;  
        } else {
            int t = 2*(i-n+1)-1 ;
            ans[t] = nums[i] ; 
            }
            
        }
    
    return ans ; 
   
        
        
        
    }
};