

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findErrorNums(int* nums, int numsSize, int* returnSize){
    *returnSize =2; 
    int *ans = malloc(sizeof(int)*(*returnSize));
    int cnt[10000]= {0} , i ;
    for(i=0 ; i<numsSize; i++){
        cnt[nums[i]-1]++; 
    }
    for(i=0 ; i < numsSize; i++){
        if ( cnt[i] ==2 ) ans[0] = i+1;
        else if( cnt[i] == 0) ans[1] =i+1 ;
    
    }
    return ans; 
    
    
}