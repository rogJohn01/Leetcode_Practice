class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        

        R = len(mat) ; C = len(mat[0]) 

        for r in range(R):

            tmp = [] 
            x = r ; y = 0
            while x < R and y < C:
                tmp.append(mat[x][y])
                x +=1 
                y +=1 

            tmp.sort() 
            x = r ; y = 0 ; i = 0 
            while x < R and y < C:
                mat[x][y] = tmp[i]
                x +=1  ; y+=1 ; i +=1 


        for c in range(1,C):

            tmp = [] 
            x = 0 ; y= c 
            while x < R and y < C:
                tmp.append(mat[x][y])
                x +=1 ; y +=1 
            tmp.sort() 
            x = 0 ; y = c ; i = 0 ; 
            while x < R and y < C: 
                mat[x][y] = tmp[i] 
                x +=1 ; y +=1 ; i +=1 
        
        return mat 
