class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        

        l = 1 ; r = max(ribbons)  
        maxv = 0 
        while l <=r: 

            m = (l+r) >>1 

            cnt = 0 
            for rib in ribbons: 
                cnt += rib//m 

            if cnt >= k: 
                l = m +1  
                maxv = max( maxv , m ) 
            else: 
                r = m-1 

        return maxv  
















