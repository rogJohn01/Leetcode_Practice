class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        import heapq as hq 
        box = [] 
        for i in range(len(heights) -1):
            gap = heights[i+1] - heights[i] 
            if gap> 0: 
                hq.heappush(box , gap)
                
                if len(box) > ladders: 
                    bricks -= hq.heappop(box) 
                    if bricks < 0: 
                        return i 
        return len(heights) -1 