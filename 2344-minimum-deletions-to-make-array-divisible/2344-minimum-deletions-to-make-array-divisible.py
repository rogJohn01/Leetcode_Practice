class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        div = reduce(math.gcd , numsDivide)
        nums.sort()
        for i, n in enumerate(nums):
            if div % n==0: 
                return i 
        return -1 