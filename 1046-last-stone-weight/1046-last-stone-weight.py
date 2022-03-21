class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        maxStone = [] 

        for stone in stones: 

            heapq.heappush(maxStone,(-stone ,stone))


        while len(maxStone) >1:

                y = heapq.heappop(maxStone)
                x = heapq.heappop(maxStone)

                if y !=x:
                    z = y[1]-x[1] 
                    heapq.heappush(maxStone , (-z,z))

        return maxStone[-1][1] if maxStone else 0
