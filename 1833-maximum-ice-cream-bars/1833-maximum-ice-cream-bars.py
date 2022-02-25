class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        
        costs.sort()
        
        cnt = 0 
        for i,c in enumerate(costs):
            
            coins -=c
            if coins ==0:
                return i+1
            elif coins <0:
                return i
        return len(costs)