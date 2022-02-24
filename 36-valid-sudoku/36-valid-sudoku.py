class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        N =9

        rows = [[0]*N for _ in range(N)]
        cols = [[0]*N for _ in range(N)]
        boxes = [[0]*N for _ in range(N)]

        for r in range(N):
            for c in range(N):

                if board[r][c] =='.':
                    continue 

                pos = int(board[r][c]) -1

                if rows[r][pos] ==1:
                    return False 
                rows[r][pos] =1 

                if cols[c][pos]==1:
                    return False 
                cols[c][pos] =1 

                idx = (r//3)*3+c//3
                if boxes[idx][pos]==1:
                    return False 
                boxes[idx][pos] =1 
        return True 



	