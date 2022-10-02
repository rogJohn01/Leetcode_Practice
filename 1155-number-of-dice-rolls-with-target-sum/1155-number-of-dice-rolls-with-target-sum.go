func numRollsToTarget(n int, k int, tar int) int {
 
    
    mod := int(math.Pow10(9)+ 7)
    dp := make([][]int , n+1) 
    for i := range dp {
        dp[i] = make([]int , tar +1 ) 
    }

    dp[0][0] =1 
    for x:= 1 ; x <= n ; x++ {
        for y :=1 ; y <= tar ; y++ { 
            for z :=1 ; z <= k ; z ++ { 
                if  z <= y {
                    dp[x][y] = (dp[x][y] + dp[x-1][y-z] ) % mod 
                }
            }
        }
    }
    return dp[n][tar] 
}