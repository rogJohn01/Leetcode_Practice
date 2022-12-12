

class Solution {
public:
    int climbStairs(int n) {
        
        if(n <=2) return n ; 
        int first =1 ; 
        int second = 2 ; 
        int third ; 
        for(int x=3 ; x<=n ; x++){
            third = first + second ; 
            first = second ; 
            second = third ; 
        }
        return third ; 
    }
};

// This approach uses O(1) space.(If the test case condition is larger than 45) 
