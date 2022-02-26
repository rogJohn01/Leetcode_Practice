class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        

        count = [0]*101
        for n in nums2:
            count[n] +=1
        nums1.sort()

        total = 0 
        countIdx = 100
        for i in range(len(nums1)):
            while count[countIdx] ==0:
                countIdx -=1 
            total += nums1[i]*countIdx 
            count[countIdx] -=1 
        return total 