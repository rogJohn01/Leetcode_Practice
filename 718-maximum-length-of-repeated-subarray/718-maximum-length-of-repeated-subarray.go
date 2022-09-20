func findLength(nums1 []int, nums2 []int) int {
    
    
    	al := len(nums1)
        bl := len(nums2) 

        dp := make([][]int , al+1) 
        for i := 0 ; i <  al+1 ; i++  {
            dp[i] = make( []int , bl+1) 
        }

        ans := 0
        for r := 1 ; r < al+1 ; r++{
            for c :=1 ; c < bl+1 ; c++ {
                if nums1[r-1] == nums2[c-1] {
                    dp[r][c] = dp[r-1][c-1]+1 
                    if dp[r][c] > ans {
                        ans = dp[r][c] 
        }
    }}}
        return ans 	


    
    
}