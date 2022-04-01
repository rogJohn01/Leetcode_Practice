class Solution:
    def spiralMatrixIII(self, R: int, C: int, rStart: int, cStart: int) -> List[List[int]]:
        
        
        move = [[0,1],[1,0],[0,-1],[-1,0]]
        dir = 0 
        maxl = 1
        length = maxl 
        row = rStart
        col = cStart 
        output = [] 


        while len(output) < R*C:
            while length:
                if 0 <= row < R and 0<= col <C:
                    output.append([row,col])
                row +=move[dir][0]
                col +=move[dir][1]
                length -=1 
            if dir & 1:
                maxl +=1 
            length = maxl 
            dir = (dir+1)% 4 
        return output 