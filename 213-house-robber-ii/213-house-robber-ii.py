class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(nums):
            a = b = 0
            for n in nums:
                a, b = b, max(a + n, b)
            return b        
        
        return max(f(nums[1:]), f(nums[:-1]), nums[0])