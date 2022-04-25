class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:


        l = 0  ; r =  max(candies) # or sum(candies)//k 

        while l < r: 

            m = (l+r+1) >>1 

            if	sum( can//m  for can in candies ) >= k:

                l =m  
            else:
                r = m-1 

        return l 
