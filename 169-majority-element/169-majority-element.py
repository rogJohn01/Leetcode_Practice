class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cntr = Counter(nums)
        tar = len(nums)/2 
        for k , v in cntr.items():
            print(k,v)
            if v >= tar:
                return k
    