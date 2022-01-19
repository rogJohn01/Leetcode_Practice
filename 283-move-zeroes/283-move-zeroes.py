class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       
            anchor = 0
            
            for i in range(len(nums)):
                
                if nums[i] != 0:
                    nums[anchor] , nums[i] = nums[i],nums[anchor]
                    anchor +=1
            