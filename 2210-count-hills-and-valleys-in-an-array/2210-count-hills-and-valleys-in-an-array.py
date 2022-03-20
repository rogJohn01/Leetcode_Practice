class Solution {
public:
    int countHillValley(vector<int>& nums) {
        
        
        
	vector<int> vec ;

	vec.push_back(nums[0]);

	for (int i=1; i <nums.size(); i++){
		if (nums[i] != nums[i-1]){
			vec.push_back(nums[i]); // the second, not the first ?
		}
	}

	int cnt =0 ; 

	for ( int i=1; i< vec.size()-1; i++ ){
		if (vec[i] >vec[i-1] and vec[i] > vec[i+1] ) cnt ++; 

		else if (vec[i] <vec[i-1] and vec[i] < vec[i+1]) cnt ++; 

	}
	return cnt ; 


    }
};