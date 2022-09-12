func bagOfTokensScore(tokens []int, pw int) int {

    
	ans ,  l , h := 0 , 0 , len(tokens)-1 
	sort.Ints(tokens) 
	
	for l <= h {
		if tokens[l] <= pw {
			ans ++ 
			pw -= tokens[l] 
			l ++ 
		} else if ans > 0 { 
			if l == h {
				break 
			}
			ans --
			pw += tokens[h]
			h -- 
		}else {
			break 
		}
	}
	return ans 
}
    
