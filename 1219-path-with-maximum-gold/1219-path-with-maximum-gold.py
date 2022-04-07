class Solution:
    def getMaximumGold(self, mat: List[List[int]]) -> int:
        
        

        def dfs(x,y):

            if x < 0 or x>=R or y <0 or y>= C:
                return 
            if mat[x][y] ==0:
                return 

            k = mat[x][y]
            self.gold += k 
            mat[x][y] = 0 
            
            self.maxGold = max( self.maxGold , self.gold )

            for a,b in [[1,0],[-1,0],[0,-1],[0,1]]:
                 dfs(x+a , y+b) 

            mat[x][y] = k 
            self.gold -=k 
        
        self.maxGold = 0 
        R = len(mat) ; C = len(mat[0])
        for r in range(R):
            for c in range(C):
                if mat[r][c] !=0:
                    self.gold = 0 
                    dfs(r,c)

        return self.maxGold 