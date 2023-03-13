class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        def combination(start, box):

            if box not in ans: 
                ans.append(box[:])

            if len(box) ==len(nums): 
                return 

            for i in range(start , len(nums)):
                if nums[i] not in box:
                    combination(i , box+[nums[i]])



        ans = []
        combination(0 , [])
        return ans 
