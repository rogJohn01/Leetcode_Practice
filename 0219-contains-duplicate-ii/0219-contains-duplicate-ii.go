func containsNearbyDuplicate(nums []int, k int) bool {
    
    seen := make(map[int]int)
    for i , n := range nums { 
        if  _ , ok := seen[n] ; ok && i-seen[n] <=k{ 
            return true 
        }
        seen[n]  = i 
        
    }    
    return false 
}
