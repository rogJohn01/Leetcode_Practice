class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = [] 
        def dfs(start ,path):

            ret.append(path)

            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]])




        dfs(0,[])
        return ret 