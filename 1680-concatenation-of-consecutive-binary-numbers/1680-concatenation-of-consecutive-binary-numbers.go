func concatenatedBinary(n int) int {
    
    
	ans :=0 
	thr :=1 
	pow :=0 
	for i :=1 ; i <=n ; i++ { 
		if i >= thr { 
			thr = thr << 1
			pow +=1 
		}
		ans = (ans << pow + i ) % 1000000007
	}
	return ans 


}