class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        import heapq as hq 
        
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        heap = [(-nums[0],0)]
        for i in range(1, len(nums)):
            
            while heap[0][1] < i-k: 
                hq.heappop(heap)
            
            dp[i] = nums[i] + dp[heap[0][1]]
            hq.heappush(heap ,( -dp[i] , i)) 
        return dp[-1]
        