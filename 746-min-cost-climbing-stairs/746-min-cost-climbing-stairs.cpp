class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
            
        
        
            int n = cost.size() ; 
            int one = cost[0] ; 
            int two = cost[1] ; 
            if(n<=2) return min(one,two) ;
        
            int three ; 
            for(auto i = 2; i <n ; i++){
                three = cost[i] + min(one,two) ; 
                one = two ; 
                two = three ; 
            }
            return min(three,one) ; 


    }
};