class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums: return []
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:  # out of the window
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            if i>k-2:
                res.append(nums[dq[0]])
        return res