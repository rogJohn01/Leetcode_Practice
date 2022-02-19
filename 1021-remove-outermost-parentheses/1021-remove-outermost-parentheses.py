class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        
        res = [] 
        bal = 0 
        i = 0 
        for j in range(len(s)):
            
            if s[j] == '(':
                bal +=1 
            elif s[j] == ')':
                bal -=1 
            if bal ==0:
                res.append(s[i+1:j])
                i = j+1 
        return ''.join(res) 