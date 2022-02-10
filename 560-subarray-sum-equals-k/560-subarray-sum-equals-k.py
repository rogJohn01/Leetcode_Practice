class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        


     
        cnt =0
        dic = {}
        dic[0] =1 
        sumv = 0 
        
        for i in range(len(nums)):
            sumv += nums[i]
            cnt += dic.get(sumv-k ,0 )
            dic[sumv] = dic.get(sumv, 0)  +1 
            
        return cnt 