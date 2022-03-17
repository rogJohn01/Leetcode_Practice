class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix) ; C = len(matrix[0])

        sl = [] 
        for r in range(R):
            for c in range(C):
                if matrix[r][c] ==0:
                    #matrix[r][c] ='#'
                    sl.append([r,c])


        for a, b in sl:

            for y in range(C):
                matrix[a][y] =0 
            for x in range(R):
                matrix[x][b] = 0

