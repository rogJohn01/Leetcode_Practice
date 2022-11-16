# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 1 ; right = n 
        while True: 

            m = (left+right)//2 

            ret = guess(m)
            if ret == -1:
                right = m -1 
            elif ret ==1: 
                left = m +1 
            else: 
                return m 