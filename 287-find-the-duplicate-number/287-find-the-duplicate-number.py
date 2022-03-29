class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
    
        cout = Counter(nums)
        for v,p in cout.items():
          if p !=1:
            return v 
        