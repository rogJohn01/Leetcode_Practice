class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = [] 
        table = {')':'('}
        for e in s:
            

            if e not in table:
                stack.append(e)

            elif stack and stack[-1] ==  table[e]:
                stack.pop()
            elif e in table:
                stack.append(e)
        
        return len(stack)
