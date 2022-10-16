func minDifficulty(jobD []int, d int) int {
 
    

	ln := len(jobD) 
	dp := make([][]int , d+1) 
	for i := range dp{
		dp[i] = make( []int , ln+1) 
	}
	maxv := 0 
	for i :=1 ; i <= ln ; i++ { 
		maxv = max( jobD[i-1] , maxv) 
		dp[1][i] = maxv 
	}

	for x := 2; x <=d ; x++ {
		for y := 1 ; y <=ln ; y++ { 
			if x > y { 
				dp[x][y] = -1 
				continue 
			}
			dp[x][y] = math.MaxInt32 
			nday := 0 
			for z := y ; z >1 ; z-- { 
				nday = max(jobD[z-1] , nday)
				if dp[x-1][z-1] != -1 {
					dp[x][y] = min( dp[x][y] , dp[x-1][z-1]+ nday) 
				}
			}
		}
	}
	return dp[d][ln] 
}

func max(a,b int) int {
    if a > b {
        return a 
    } else { 
        return b 
    }
}
func min(a,b int) int { 
    if a > b {
        return b 
    } else { 
        return a 
    }
}
