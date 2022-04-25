class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        l = 1  ; r =  max(candies) 

        while l <= r: 

            m = (l+r) >>1 

            if	sum( can//m  for can in candies ) >= k:

                l = m+1
            else:
                r = m-1 

        return r 

