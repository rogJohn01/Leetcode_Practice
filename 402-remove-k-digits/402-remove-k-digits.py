class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        stack = [] 
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -=1
            stack.append(n)
        
        fstack = stack[:-k] if k  else stack 
        
        return "".join(fstack).lstrip('0' ) or '0'