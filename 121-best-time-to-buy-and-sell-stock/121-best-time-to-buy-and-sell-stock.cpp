class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int maxcur =0 ;
        int maxfar = 0;
        
        for(int i=1 ; i<prices.size() ; ++i){
            
            maxcur = max( 0 , maxcur + prices[i]- prices[i-1]);
            maxfar = max( maxfar , maxcur );
        }
        return maxfar ;
        
        
        
    }
};