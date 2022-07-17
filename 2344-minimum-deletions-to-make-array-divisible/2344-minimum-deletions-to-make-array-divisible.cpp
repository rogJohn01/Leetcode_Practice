class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& numsDivide) {
     

        int a = numsDivide[0] ; 
        for(int i =1; i < numsDivide.size() ; i++) 
            a = gcd(a , numsDivide[i]) ; 

        sort(nums.begin() , nums.end()); 
        for(int j=0 ; j< nums.size() ; j++)
            if( a % nums[j] ==0) return j ; 
        return -1; 


        
        
    }
};