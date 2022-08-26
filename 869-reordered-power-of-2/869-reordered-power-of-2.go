func reorderedPowerOf2(n int) bool {
    
    
	cntr := func(n int) [10]int {
		var res [10]int
		for n > 0 {
			res[n%10]++
			n /= 10
		}
		return res
	}

	xcntr := cntr(n)
	for i := 0; i < 31; i++ {
		if xcntr == cntr(1<<i) {
			return true 
		}
	}
	return false 

    
}