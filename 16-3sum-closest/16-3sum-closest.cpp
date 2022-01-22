class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        int diff = INT_MAX;
        int sz = nums.size();
        sort(begin(nums) , end(nums));
        for (int i =0; i <sz && diff !=0; ++i){
            int low = i+1;
            int high = sz-1;
            while (low < high) {
                
                int sum = nums[i]+ nums[low]+ nums[high];
                
                if (abs(target - sum) < abs(diff)) {
                    diff = target -sum; 
                }
                if (sum <target){
                    ++low;
                } else {
                    --high;
                }
                
            }
        }
        return target - diff; 
        
    }
};