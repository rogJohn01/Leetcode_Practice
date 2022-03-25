class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
           
        bas = []
        for i, v in enumerate(nums):
            
            if v ==target:
                bas.append(i)
                
        if len(bas) >=2:
            return [bas[0] , bas[-1] ]
        
        if len(bas)==1:
            return [ bas[0] , bas[0]   ] 
        
        if len(bas) ==0:
            return [-1,-1 ]
                
            
       