class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        
        vector<int> ret; 
        deque<int> deq; 
        
        for( int i =0; i < nums.size(); ++i){
            
            if(!deq.empty() && i-k >=0 && deq.front()==nums[i-k]){
                deq.pop_front();
            }
            while(!deq.empty() && deq.back() < nums[i] ){
                deq.pop_back();
            }
            deq.push_back(nums[i]);
            
            if (i>=k-1) ret.push_back(deq.front());
        }
        return ret; 
        
        
    }
};