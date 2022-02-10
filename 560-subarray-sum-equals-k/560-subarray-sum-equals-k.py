class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        


     
        cnt =0
        dic = {}
        dic[0] =1 
        sumv = 0 
        
        for i in range(len(nums)):
            sumv += nums[i]
            if (sumv-k) in dic:
                cnt += dic[sumv-k]
            dic[sumv] = dic.get(sumv, 0)  +1 
            
        return cnt 