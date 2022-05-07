class Solution {
public:
    int jump(vector<int>& nums) {

     
    int jumpend =0 ;
    int furthest =0; 
    int jump = 0 ; 
    int i = 0 ; 
    while(i < nums.size()-1 ) {
        
        furthest = max(furthest , i+nums[i] ) ; 
        if ( i ==jumpend){
            jumpend = furthest ;
            jump ++;  }

        i++; }

    return jump; 

        
        
        
    }
};