class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        
        corner = {(0,p):2 , (p,p):1 , (p,0):0  }
        [cx , cy] = [ p, q ] 
        rev = False 
        while True: 

            if (cx,cy) in corner.keys():
                return  corner[(cx,cy)] 

            cx =  0  if cx ==p else p
            if rev: 
                cy -=q 
            else: 
                cy += q
            if cy > p: 
                cy = p - (cy-p)
                rev = True 
            elif cy < 0: 
                cy = -cy 
                rev = False 