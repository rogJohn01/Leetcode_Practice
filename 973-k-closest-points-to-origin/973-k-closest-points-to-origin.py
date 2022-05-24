class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        heap = [] 
        for x, y in points:
            d =  (x**2+ y**2)**(0.5)  
            heappush(heap , (d, [x,y] ) )

        ans = [] 
        while k: 
            out =  heappop(heap) 
            ans.append( out[1]) 
            k -=1 

        return ans     