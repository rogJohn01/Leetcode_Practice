class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
          
            
        nums = numbers 
        # almost typical hashmap approach !!  
        
        for idx, n in enumerate(nums):
            
            k = target -n 
            tar = self.binarySearch(nums,k)
            if tar != -1:
                if idx ==tar:
                    return [idx+1, tar+2]
                return [idx+1,tar+1 ]
        
        

    def binarySearch(self, nums, k):
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