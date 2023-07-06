class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        mindq, maxdq = deque(), deque()
        l = cnt= 0
        for r in range(len(nums)):
            while mindq and nums[mindq[-1]] > nums[r]:
                mindq.pop()
            mindq.append(r)

            while maxdq and nums[maxdq[-1]] < nums[r]:
                maxdq.pop()
            maxdq.append(r)

            while nums[maxdq[0]] - nums[mindq[0]] > 2:
                l += 1
                if l> mindq[0]:
                    mindq.popleft()
                if l > maxdq[0]:
                    maxdq.popleft()

            cnt += r - l + 1
        return cnt 