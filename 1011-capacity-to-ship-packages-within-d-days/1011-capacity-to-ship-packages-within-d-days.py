class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:         
        
        
        left , right = max(weights) , sum(weights)
        while left < right:
            mid = left + (right-left)//2
            
            if self.packaging(mid ,weights ,days):
                right = mid 
            else:
                left =mid +1 
        return left 
        
        
        
        
    def packaging(self, size ,weights ,days ):
        
        edays = 1
        total = 0
        for box in weights:
            total += box 
            if total > size:
                total = box
                edays +=1 
                if edays > days:
                    return False 
        return True 