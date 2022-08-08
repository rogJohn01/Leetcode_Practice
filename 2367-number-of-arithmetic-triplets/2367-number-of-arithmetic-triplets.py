class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        

        nl = len(nums) 
        ans = 0 
        for i in range(nl):
            for j in range(i+1, nl):
                for k in range(j+1, nl): 
                    if nums[j]-nums[i] == nums[k]- nums[j] == diff:
                        ans +=1 
        return ans 