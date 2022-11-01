func findBall(mat [][]int) []int {
    
    
    ans := make([]int , len(mat[0]))
    
    for i := 0 ; i < len(ans) ; i++ { 
        ans[i] = walk(mat,i,0)
    }
    return ans 
    
}

func walk(mat[][]int , x, y int ) int { 

    if y == len(mat){
        return x
    }
    if mat[y][x] == 1 {
        if x == len(mat[y]) -1 || mat[y][x+1] == -1 {
            return -1 
        }
        return walk(mat , x+1 , y+1)
    }
    if x == 0 || mat[y][x-1] == 1 {
        return -1 
    }
    return walk(mat, x-1 , y+1)





}