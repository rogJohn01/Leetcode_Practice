class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
            if len(nums) <=3:
                for i,v in enumerate(nums):
                    if v==target:
                        return i
                return -1 

            sortnums = sorted(nums)
            k = sortnums.index(nums[0]) 

            tar = self.binarySearch(sortnums,target)
            if tar ==-1:
                return tar 

            ans = (tar-k+len(nums))%len(nums) # ne  
            return ans 

        
    def binarySearch(self,nums, k):
            left , right = 0 , len(nums)-1 
            while left <= right:
                mid = (left +right)//2
                if nums[mid] == k:
                    return mid 
                elif nums[mid]> k:
                    right = mid-1
                else:  
                    left = mid+1
            return -1 


          