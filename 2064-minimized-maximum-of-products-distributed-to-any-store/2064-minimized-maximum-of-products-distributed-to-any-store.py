class Solution:
    def minimizedMaximum(self, k: int, quant: List[int]) -> int:
        
        



        l = 0  ; r = max(quant)

        minv = max(quant)
        while l <=r:
            cnt = k     
            m = (l+r ) >>1
            if m ==0:
                l = m +1
                continue 
            
            for q in quant:
                    
                q /=  m
                cnt -= math.ceil(q) 

            if cnt  >=  0:
                r = m -1  
                minv = min( minv , m ) 
            else: 
                l = m +1  

        return minv 


