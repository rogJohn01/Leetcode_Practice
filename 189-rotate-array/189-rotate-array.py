class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        nlen = len(nums)
        a=[0]*nlen 
        
        for i in range(nlen):
            a[(i+k)%nlen] = nums[i]
        
        nums[:] = a 