class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        
         
        if k==1:
            return 0 
        
        
        minv= 100001
        nums.sort()
        for i in range(0, len(nums)-k+1):
            box =nums[i:i+k]
            dif = box[-1]- box[0]
            minv = min(dif,minv)
        return minv 