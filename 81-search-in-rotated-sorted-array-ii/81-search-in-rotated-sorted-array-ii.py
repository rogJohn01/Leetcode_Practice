class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        nums.sort()
        return self.binarySearch(nums,target )
        
        
        
    def binarySearch(self,nums, k):
                left , right = 0 , len(nums)-1
                while left <= right:
                    mid = (left +right)//2
                    if nums[mid] == k:
                        return True 
                    elif nums[mid]> k:
                        right = mid-1
                    else:
                        left = mid+1
                return False 
