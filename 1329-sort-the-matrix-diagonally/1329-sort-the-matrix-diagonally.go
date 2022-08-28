func diagonalSort(mat [][]int) [][]int {
        
    	
	R := len(mat) 
	C := len(mat[0]) 
	diag := make(map[int][]int) 

	for r:=0 ; r < R ; r++ { 
		for c:=0 ; c < C ; c ++ { 
			diag[r-c] = append(diag[r-c] , mat[r][c] )
		}
	} 
	for _ , v:= range diag { 
		sort.Ints(v)  
	} 
	for r:=0; r < R ; r++ { 
		for c:=0 ; c< C; c++ { 
			mat[r][c] = diag[r-c][0] 
			diag[r-c] = diag[r-c][1:]
		}
	}
	return mat 
}
    
