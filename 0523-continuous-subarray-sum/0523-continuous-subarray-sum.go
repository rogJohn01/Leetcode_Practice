func checkSubarraySum(nums []int, k int) bool {
    
    box := map[int]bool{0:true} ; 
    for i := 1 ; i < len(nums) ; i++ { 
        nums[i] += nums[i-1] ; 
        if box[nums[i] %k] {
            return true 
        }
        box[nums[i-1]%k] = true 
    
    }
    return false 
    
    
}