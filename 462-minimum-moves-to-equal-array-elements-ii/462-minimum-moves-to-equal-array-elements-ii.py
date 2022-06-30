class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort() 
        sumv = 0 
        l , r = 0, len(nums)-1 
        while l<r: 
            sumv += nums[r]-nums[l] 
            l +=1 ; r -=1 

        return sumv 