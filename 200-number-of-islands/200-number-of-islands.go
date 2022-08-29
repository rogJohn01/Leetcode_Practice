

func numIslands(mat [][]byte) int {
    
    
    
    
	R := len(mat)
	C := len(mat[0]) 
	ans := 0 
	for r:=0; r <R ; r++ { 
		for c:=0 ; c < C ; c++ { 
			if mat[r][c] ==49 { 
				dfs( r,c ,mat) 
				ans ++ 
			}
	
		}}
    return ans 

}

func dfs(x int,y int , mat [][]byte) {
    
        
	R := len(mat)
	C := len(mat[0]) 
	if 0<= x && x< R && 0<= y && y < C {
		if mat[x][y] ==49 {
			mat[x][y] = 0 
			dfs(x-1,y, mat)
			dfs(x+1,y , mat)
			dfs(x,y-1 , mat )
			dfs(x,y+1, mat ) 
		}
	}


    
    
    
}