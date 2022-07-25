class Solution:
    def searchRange(self, nums: List[int], tar: int) -> List[int]:
        
        if not nums: return [-1,-1]
        nl = len(nums)
        lk = bisect.bisect_left(nums,tar)
        lk = lk if 0<=lk <nl and nums[lk]==tar else -1
        rk = bisect.bisect_right(nums,tar)
        print(rk)
        rk = rk -1 if  0<=rk-1<nl and nums[rk-1] ==tar else -1 
        return [lk,rk ]