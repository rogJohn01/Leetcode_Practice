class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        
        def helper(s):
            stack = [] 
            for e in s:

                if e =='#' and stack:
                    stack.pop()
                elif e !='#':
                    stack.append(e)
            return stack 

        return helper(s) == helper(t)