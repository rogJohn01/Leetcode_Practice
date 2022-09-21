func sumEvenAfterQueries(nums []int, queries [][]int) []int {
    

    ans , sum := []int{} , 0 

    for _, n := range nums {
        if n % 2 ==0 {
            sum += n }
        }
    for _ , q := range queries {
        v, ix := q[0] , q[1] 
        if nums[ix] % 2 == 0 {
            sum -= nums[ix] 
        }
        nums[ix] += v
        if nums[ix] % 2 == 0 { 
            sum += nums[ix]
        }
        ans = append(ans , sum)
    }
    return ans 
    
    
}