class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            
            cntr = Counter(nums)
            
            for k in cntr.keys():
                
                if cntr[k] ==1:
                    return k 