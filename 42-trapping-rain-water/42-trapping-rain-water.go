func trap(h []int) int {
    
    max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

    
	hn := len(h)
	lw := make([]int, hn)
	rw := make([]int ,hn) 
	for l := 1 ; l < hn ; l++ { 
        lw[l] = max( lw[l-1] , h[l-1])
		}
	
	for r:=hn-2 ; r >=0; r-- { 
		rw[r] = max( rw[r+1] , h[r+1] )
	}

	ans := 0 
	for i := range h {
        wlev := min( lw[i] , rw[i] )
		if wlev > h[i] { 
			ans += wlev - h[i] }
	}
	return ans 


    
    
    
    
}