class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        


        ans = [] 
        for k, tr in queries: 
            tmp = [] 
            for i , n in enumerate(nums): 
                tmp.append( [ int(n[-tr:]) , i])
            ans.append( sorted(tmp)[k-1][1] )
        return ans 