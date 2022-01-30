class Solution:
    def maximum69Number (self, num: int) -> int:
        
        nums = str(num)
        ret = [] 
        mode =0 
        for i in range(len(nums)):
             
            if nums[i] =='6' and mode==0:
                ret.append( '9' ) 
                mode +=1 
            else:
                ret.append(nums[i])
        return int(''.join(ret))