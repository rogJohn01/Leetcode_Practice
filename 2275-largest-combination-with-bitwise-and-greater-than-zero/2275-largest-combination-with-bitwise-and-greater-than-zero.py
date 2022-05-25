class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        
        

        bit = [0]*25
        for can in candidates: 

            x = 24  
            while can: 

                if can &1 ==1: 

                    bit[x] +=1 
                can = can >>1 
                x -=1 
        
        return max(bit)

