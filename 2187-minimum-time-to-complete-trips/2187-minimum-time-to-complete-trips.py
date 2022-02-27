class Solution:
    def minimumTime(self, time: List[int], Ttrips: int) -> int:
        
          

        l =0 ; r = min(time)*Ttrips 
        while l< r:
            m = (l+r)//2 ; trips = 0 
            for t in time:
                trips += m//t
            if trips < Ttrips:
                l = m +1 
            else:
                r = m; 
        return l 