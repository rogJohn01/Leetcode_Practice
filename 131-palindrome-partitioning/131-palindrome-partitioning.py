class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = [] 
        def backtrack(start , ret):
            
            if start ==len(s):
                ans.append(ret[:])
            
            for i in range(start ,len(s)):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    backtrack(i+1 , ret+[cur])
                    
                    
        backtrack(0,[])
        return ans 