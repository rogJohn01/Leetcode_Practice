class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        
        ans = [] 
        for i in range(1,len(nums)+1):
            
            left = len(set(nums[:i]))
            right = len(set(nums[i:]))
            
            ans.append(left-right)
            
        return ans  