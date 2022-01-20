class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            
            return nums[0]
        
        
        cnt = 0
        maxv = 0 # no -sys.maxsize
        for i in range(len(nums)):

            if nums[i] ==1:
                cnt +=1
                maxv = max(cnt, maxv)

            if nums[i] ==0 and nums[i-1] ==1: # there may be an edge case, here! 
                cnt =0 
        return maxv 