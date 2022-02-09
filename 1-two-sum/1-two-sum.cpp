class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        
        map<int, int> hash; 
        vector<int> ret; 
        
        for(int i=0; i <nums.size(); ++i){
            
            int pair = target - nums[i];
            if( hash.find(pair) != hash.end() ){
                ret.push_back(hash[pair] );
                ret.push_back(i);
                
                return ret;
            }
            hash[nums[i]] =i; 
        }
        
        
        
        return ret; 
    }
};