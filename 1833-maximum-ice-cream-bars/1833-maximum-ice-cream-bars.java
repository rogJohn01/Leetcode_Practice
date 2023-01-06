class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        
        
        sort(costs.begin() , costs.end() ) ; 

        int ans =0 ; 
        for(auto c:costs){
            coins -= c ;
            ans++ ; 
            if(coins ==0) return ans ; 
            else if(coins < 0) return ans-1; 
        } return ans; 

    }
};