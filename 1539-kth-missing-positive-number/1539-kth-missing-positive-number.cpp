class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        
        for(int i =1 ; i <=  2000 ; i++){
            if( !count(arr.begin() , arr.end() , i)){
                k--; 
                if(!k){
                    return i ; 
                }
            }
        }
        return 0; 
        
    }
};