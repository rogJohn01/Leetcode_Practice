class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        
        heapq.heapify(weight)
        apples = units = 0
        
        while weight and units + weight[0] <= 5000:
            units += heapq.heappop(weight)
            apples +=1 
        return apples 