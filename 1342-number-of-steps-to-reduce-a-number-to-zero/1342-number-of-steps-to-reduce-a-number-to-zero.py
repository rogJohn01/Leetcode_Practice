class Solution:
    def numberOfSteps(self, num: int) -> int:

        
        cnt = 0 
        while num:
            if  bin(num)[-1] =='0':

                num = num >>1 
                cnt +=1 
            elif bin(num)[-1] =='1':
                num -=1
                cnt +=1        
                
        return cnt


            