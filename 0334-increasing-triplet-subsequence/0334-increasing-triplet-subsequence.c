

bool increasingTriplet(int* nums, int numsSize){

    int first = INT_MAX;
    int second = INT_MAX;
    for(int i=0; i < numsSize ; i++){
        int n = nums[i];
        if( n <= first) first = n; 
        else if( n <= second)  second = n ; 
        else return true ; 
    }
    return false ; 
}