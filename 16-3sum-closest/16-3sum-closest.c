#define ABS(x) ((x)<0?-(x):(x))

int abs(int a){
    return a > 0 ? a:-a ; 
}

int comparefn( const void* a, const void* b)
{
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}

int threeSumClosest(int* nums, int numsSize, int tar) {
    qsort(nums, numsSize, sizeof(int), comparefn);
    int i, l,r , diff, mdiff = INT_MAX;
    for(i = 0 ; i < numsSize ; i++)
    {
        l = i + 1;
        r = numsSize - 1;
        while(l < r )
        {
            diff = nums[i] + nums[l] + nums[r] - tar;
            if(diff == 0){
                return tar;
            }
            else{
                if(abs(diff) < abs(mdiff))
                {
                    mdiff = diff;
                }
                if(diff < 0)
                {
                    l++;
                }
                else
                {
                    r--;
                }
            }
        }
    }
    return tar + mdiff;
}