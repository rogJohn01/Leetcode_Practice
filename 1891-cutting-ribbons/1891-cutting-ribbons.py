class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        

        l = 1 ; r = max(ribbons)  
        while l <=r: 

            m = (l+r) >>1 

            cnt = 0 
            for rib in ribbons: 
                cnt += rib//m 



            if cnt >= k: 
                l = m +1  
            else: 
                r = m-1 

        return  r    

