class Solution:
    def reverse(self, x: int) -> int:
        
        if x ==0:
            return 0 
        
        minus = False 
        if str(x)[0] =='-':
            
            minus = True 
            x = str(x)[1:]
            
        
        if str(x)[-1] == '0':
            x = str(x)[:-1]
        
        x = int( str(x)[::-1] )        
        
        if x >= (2**31 -1):
            return 0 
        
        return  -x if minus else x
        
       
        # test case ->  x = -120 