from collections import defaultdict
class Solution:
    def solveSudoku(self, mat):
       

        row = defaultdict(list)
        col = defaultdict(list) 
        box = defaultdict(list) 
        cnt = 0 
        R = C = 9
        for r in range(R):
            for c in range(C):
                if mat[r][c] !='.':
                    n = mat[r][c] 
                    row[r].append(n) 
                    col[c].append(n) 
                    box[(r//3, c//3)].append(n)
                    cnt +=1 

        left = 81-cnt 
        def backtrack(lc):

            if lc == left:
                return mat 

            for r in range(R):
                for c in range(C):
                    if mat[r][c] =='.':

                        dup = True 
                        for i in range(1,10): 
                            i = str(i)
                            if i not in row[r] and i not in col[c] and i not in box[(r//3, c//3)]:
                                dup = False 
                                row[r].append(i)
                                col[c].append(i) 
                                box[(r//3,c//3)].append(i) 
                                mat[r][c] = str(i)  
                                if backtrack(lc+1):
                                    return True 
                                row[r].pop()
                                col[c].pop()
                                box[(r//3,c//3)].pop() 
                                mat[r][c] = '.'
                        return False 

        backtrack(0)
        return mat 