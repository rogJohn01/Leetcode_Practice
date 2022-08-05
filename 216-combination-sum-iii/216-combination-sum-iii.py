class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        

        nums = [ i for i in range(1,10) ] 
        def backtrack(tot , path , start, cnt ): 

            if cnt ==k:
                if tot ==0:
                    ans.append(path[:]) 
                return 

            if tot < 0: return 

            for i in range(start,len(nums)):

                backtrack( tot- nums[i] ,path+[nums[i]]  , i +1 , cnt+1)  


        ans = []
        backtrack( n  , [] , 0, 0) 
        return ans 