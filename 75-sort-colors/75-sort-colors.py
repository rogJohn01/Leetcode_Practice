class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = 0 
        b = len(nums)


        while w < b: 


            if nums[w] ==0:

                nums[w] , nums[r] = nums[r] , nums[w]
                r +=1 ; w +=1 

            elif nums[w] ==2:
                b -=1 
                nums[w] ,nums[b] = nums[b] , nums[w]
            elif nums[w] ==1:
                w +=1 