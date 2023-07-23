class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        maxv = 0
        while len(nums) >=2: 
            b = nums.pop()
            a = nums.pop() 
            if a <=b: 
                c = a+b
                nums.append(c)
                maxv = max(maxv , c)
            else: 
                nums.append(a)
            maxv = max(maxv , max(a,b))
        
        if nums: 
            maxv = max(maxv, nums.pop() ) 
        
        return maxv 