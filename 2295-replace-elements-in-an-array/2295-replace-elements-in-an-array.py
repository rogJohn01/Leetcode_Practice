class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        



        dic = { n: idx for idx , n in enumerate(nums) } 

        for a,b in operations: 
            nums[dic[a]] = b 
            dic[b] = dic.pop(a)
        
        return nums 