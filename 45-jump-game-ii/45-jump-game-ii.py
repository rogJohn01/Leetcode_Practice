class Solution:
    def jump(self, nums: List[int]) -> int:
      
    

        jumpend = furthest = jump = 0 

        for i in range(len(nums)-1): 

            furthest = max(furthest , i+nums[i] ) 
            if i ==jumpend:
                jumpend = furthest 
                jump +=1 

            i+=1 

        return jump 