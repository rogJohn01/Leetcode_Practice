class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        
        
        weight.sort()
        cnt , cur = 0 ,0 
        for w in weight:
            
            cur += w
            if cur > 5000:
                return cnt 
            else:
                cnt +=1 
        return cnt 