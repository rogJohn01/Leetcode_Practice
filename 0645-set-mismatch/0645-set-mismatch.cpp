class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        unordered_map<int,int> map ; 
        int first , second ; 
        for(int n:nums) map[n]++ ;
        
        for(int i=1 ; i <= nums.size() ; i++){
            if (map[i] ==2 ) first = i;
            else if(map[i] ==0 ) {
                second = i ;
            }
        }
        return {first, second} ; 
    }
};