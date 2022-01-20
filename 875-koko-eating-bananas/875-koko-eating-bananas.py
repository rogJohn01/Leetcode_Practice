class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        left = 1 # why 1 ? 
        right = max(piles)
    
        while left <right:  
            
            
            mid = (left+right)//2
            hour = 0 

            
            for banana in piles:
                hour += math.ceil(banana/mid)
                
            
            if hour <=h:
                right = mid
            else:
                left = mid +1 
            
        return right 