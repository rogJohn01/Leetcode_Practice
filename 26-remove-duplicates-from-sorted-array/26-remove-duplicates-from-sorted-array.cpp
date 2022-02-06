class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
     
        
       if (nums.size() == 0) return 0;
  
  int walker = 0, runner = 0, size = nums.size();
  while (runner < size) {
      if (nums[walker] == nums[runner]) ++runner;
      else {
          ++walker;
          nums[walker] = nums[runner];  
          ++runner;
            }
        }
         nums.erase(nums.begin() + walker + 1, nums.end());
  
    return nums.size();
    }
};