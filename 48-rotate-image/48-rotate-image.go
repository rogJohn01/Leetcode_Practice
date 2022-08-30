func rotate(mat [][]int)  {
    
    transpose(mat)
    row_reverse(mat)
}

func transpose(mat [][]int) { 
	R := len(mat) 
	//C := len(mat[0]) 

	for r :=0 ; r < R ; r++ { 
		for c:=0 ; c < r; c++ { 
			mat[r][c] , mat[c][r] = mat[c][r] , mat[r][c] 
		}}
	}

func row_reverse(mat [][]int) {

	for _, row := range mat {
		for i, j := 0, len(row)-1; i < j; i, j = i+1, j-1 {
			row[i], row[j] = row[j], row[i]
		}
	}
}

