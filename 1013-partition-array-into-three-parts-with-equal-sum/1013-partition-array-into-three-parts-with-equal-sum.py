class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    
        s = sum(arr)
        
        if s % 3 !=0:
            return False 
        
        culsum ,cnt = 0 , 0 
        
        for num in arr:
            
            culsum += num 
            if culsum == s//3:
                culsum = 0
                cnt +=1
        
        return cnt >=3
            