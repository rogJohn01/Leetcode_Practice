class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq as hq 
        heap = [] 
        while nums:
            a = nums.pop()
            hq.heappush(heap , (-a, a))

        while k:
            bm,b = hq.heappop(heap) 
            k -=1 ; 

        return b 
