class Solution:
    def makeGood(self, s: str) -> str:
        
        
        stack = []
        #stack.append(s[0])
        for i in range(len(s)):
            
            if  stack and stack[-1].swapcase() == s[i]:
                stack.pop()
            
            else:
                stack.append(s[i])
        return ''.join(stack)