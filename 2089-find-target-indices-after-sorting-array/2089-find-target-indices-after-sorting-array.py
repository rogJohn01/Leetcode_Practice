class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
            
            ret = [] 
            nums.sort()
            for i,v in enumerate(nums):
                
                if v ==target:
                    ret.append(i)
            return ret 