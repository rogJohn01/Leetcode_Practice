class Solution:
    def minimizedMaximum(self, k: int, quant: List[int]) -> int:
        
        



        l = 1  ; r = max(quant)

        minv = max(quant)
        while l <r:
            cnt = k     
            m = (l+r ) >>1
            
            for q in quant:
                    
                q /=  m
                cnt -= math.ceil(q) 

            if cnt  >=  0:
                r = m 
                minv = min( minv , m ) 
            else: 
                l = m +1  

        return l 


