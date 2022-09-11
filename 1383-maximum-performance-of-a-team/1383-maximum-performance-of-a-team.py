class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        

        engs = list(zip(efficiency, speed))
        engs.sort(reverse = True) 
        heap = [] 
        ans = ssum = 0 
        for e ,s in engs:
            ssum += s
            heappush(heap, s)
            if len(heap) > k:
                ssum -= heappop(heap)
            ans = max(ans, ssum*e)
        return ans % (10**9 + 7) 