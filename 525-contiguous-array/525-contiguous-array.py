class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        cnt = maxl = 0
        dic = {0:0}
        for idx, n in enumerate(nums ,1 ):
            
            if n ==0:
                cnt +=1 
            elif n==1:
                cnt -=1 
            
            if cnt in  dic:
                maxl = max(maxl , idx - dic[cnt])
            else:
                dic[cnt] = idx
        return maxl 