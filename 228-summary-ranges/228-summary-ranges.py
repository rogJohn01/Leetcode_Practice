class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        

        ret = []
        N = len(nums)
        start = end = 0 
        while start < N and end < N:

            if end+1 < N and nums[end+1] == nums[end]+1:
                end +=1 


            elif  start == end:
                ret.append(str(nums[start]))
                start = end+1
                end  +=1 


            else:
                ret.append(str(nums[start])+'->'+str(nums[end]) )
                start = end+1
                end  +=1 
        return ret 