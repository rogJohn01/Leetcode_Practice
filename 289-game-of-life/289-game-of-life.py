class Solution:
    def gameOfLife(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        dir = [[1,0] ,[-1,0] ,[0,1] , [0,-1] , [1,1] , [1,-1] , [-1,1] ,[-1,-1] ] 
        R = len(mat) ; C = len(mat[0])
        store = [] 
        for r in range(R):
            for c in range(C):
                if mat[r][c] ==1:
                    # check 8directions 
                    cnt = 0 
                    for a,b in dir:
                        nx , ny = r+a , c+b 
                        if nx < 0 or nx>=R or ny <0 or ny>=C:
                            continue 


                        if mat[nx][ny] ==1:
                            cnt +=1 

                    if cnt <2:
                        store.append([r,c,0])
                    elif cnt >3:
                        store.append([r,c,0])

                if mat[r][c] ==0:
                    cnt = 0
                    for a,b in dir:
                        nx , ny = r+a , c+b 
                        if nx < 0 or nx>=R or ny <0 or ny>=C:
                            continue 

                        if mat[nx][ny] ==1:
                            cnt +=1 

                    if cnt ==3:
                        store.append([r,c,1])

        for r, c , v in store:
            mat[r][c] = v

