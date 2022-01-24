class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
            
            
        nums = [i for i in range(1,n+1)]
        ret = [] 
        def dfs( start, path):

            if len(path) == k:
                ret.append(path)
                return 

            for i in range(start, len(nums)):
                    dfs(i+1 , path+[nums[i]])


        dfs(0, [] )
        return ret 

