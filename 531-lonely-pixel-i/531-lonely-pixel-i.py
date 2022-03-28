class Solution:
    def findLonelyPixel(self, mat: List[List[str]]) -> int:
        
        

        pix = 0 
        loco = [] ; R =len(mat) ; C =len(mat[0])
        for r in range(R):
            for c in range(C):
                if mat[r][c] =='B':
                    lonely = True 
                    for r1 in range(R):
                        if r1 !=r and mat[r1][c] =='B':
                            lonely = False 
                    for c1 in range(C):
                        if c1 !=c and  mat[r][c1] == 'B':
                            lonely = False 
                    if lonely:
                        pix +=1 
        return pix 