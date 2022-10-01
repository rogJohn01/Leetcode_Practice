func numDecodings(s string) int {
    
    
	dp := make([]int , len(s)+1 ) 
	dp[0] =1 
	if s[0] != '0' {
		dp[1] =1 }
	for i :=2 ; i < len(dp) ; i++ {
        one, _ := strconv.Atoi(s[i-1:i] )
	    two,_  := strconv.Atoi(s[i-2:i] ) 
       
		if one >=1 {
			dp[i] += dp[i-1] 
		}
		if two >= 10 && two <=26 {
			dp[i] += dp[i-2] 
		}
    }
	return dp[len(s)] 
}


    
