class Solution {
public:
    vector<bool> ans ; 
    
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        
        
        int maxv = *max_element(candies.begin(), candies.end() ) ; 
        for(int c:candies){
            if(c+extraCandies >= maxv){
                ans.push_back(true) ;
            }else {
                ans.push_back(false) ;
            }
        }
        return ans; 
    }
};