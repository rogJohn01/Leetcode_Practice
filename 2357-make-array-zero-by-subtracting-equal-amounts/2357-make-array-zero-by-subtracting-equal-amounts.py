class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        

        inf = float('inf') 
        cnt = 0 
        while True: 


            minv = inf 
            for n in nums:

                if n !=0 and n < minv: 
                    minv = n 
            if minv==inf:
                break 

            for i  in range(len(nums)):

                if nums[i] != 0:
                    nums[i] -= minv 



            cnt +=1 

        return cnt 