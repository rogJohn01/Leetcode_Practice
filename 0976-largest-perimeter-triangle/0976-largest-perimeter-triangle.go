func largestPerimeter(nums []int) int {
    
    sort.Slice(nums, func(x,y int) bool {
        return nums[x] > nums[y]
    })
    for i := 0 ; i < len(nums) -2 ; i++ { 
        if nums[i] < nums[i+1] + nums[i+2]{
            return nums[i] + nums[i+1] + nums[i+2]
        }
    }    
    return 0 
}