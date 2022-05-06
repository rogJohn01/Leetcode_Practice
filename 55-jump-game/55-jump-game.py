class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        ln = len(nums)
        goal = ln -1 
        for i in range(ln-1, -1,-1):
            if i+nums[i] >= goal:
                goal = i 
        
        return goal ==0 