class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        k = 0 
        while True:
            k +=1 
            pre =k 
            mode =1 
            for n in nums:
                pre +=n 
                if pre <1:
                    mode =0 
                    break 
            if mode ==1:
                return k 