func isToeplitzMatrix(matrix [][]int) bool {
    R := len(matrix)
    C := len(matrix[0])
    
    for i := 0; i < R - 1; i++ {
        for j := 0; j < C - 1; j++ {
            if matrix[i][j] != matrix[i + 1][j + 1] {
                return false
            }
        }
    }
    
    return true
}