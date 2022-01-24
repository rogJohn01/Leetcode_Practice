class Solution:
    def mySqrt(self, x: int) -> int:
        

        left ,right = 0, x 
        while left <= right: 
            mid = (left+right)//2
            
            if mid*mid ==x:
                return mid 
            if mid*mid >x:
                if (mid-1)*(mid-1) <x:
                    return mid-1
                right = mid-1
            if  mid*mid <x:
                left = mid+1
        return x 
                
