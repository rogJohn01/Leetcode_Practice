class Solution:
    def totalNQueens(self, N: int) -> int:
        
        def valid(row, i): 

            for j in range(i):
                if ( row[i] == row[j] ) or ( abs(i-j) == abs(row[i]-row[j])):
                    return False 
            return True 

        def backtrack(row,i ):
            global cnt 
            if i == N:
                cnt +=1 
                return 

            for c in range(N): 

                row[i] = c 
                if valid(row,i):
                    backtrack(row , i+1) 
        global cnt 
        cnt = 0 
        row= [0]*N 
        backtrack(row,  0) 
        return cnt 