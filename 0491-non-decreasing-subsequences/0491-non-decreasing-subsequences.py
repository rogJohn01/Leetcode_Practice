class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        ans = set()
        box = [] 

        def backtrack(ix):
            
            if ix == len(nums):
                if len(box) >=2:
                    ans.add(tuple(box))
                return 

            if not box or box[-1] <= nums[ix]:
                    box.append(nums[ix])
                    backtrack(ix+1)
                    box.pop() 
            
            backtrack(ix+1)
        backtrack(0)
        return ans 