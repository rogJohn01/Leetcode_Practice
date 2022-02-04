class Solution {
public:
    int minStartValue(vector<int>& nums) {
          int n = nums.size();
    int m = 200;
    
    int left = 1, right = m*n+1;
    
    while (left <right){
        int middle = (left +right) /2;
        int total = middle;
        bool isValid =true;
        
        for (int num : nums){
            total += num;
            
            
            if (total <1){
                isValid = false;
                break;
            }
        }
        if (isValid){
            right = middle;
        }
        else {
            left = middle +1;
        }
    
    }

    return left;
    }
};