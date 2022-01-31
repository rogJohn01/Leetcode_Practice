class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> ret;
        int sumv = 0;
        for (auto n:nums){
            sumv +=n; 
            ret.push_back(sumv);
        }
        
    return ret;
    }       
};