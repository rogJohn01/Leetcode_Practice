class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        retbox = [] 
        def backtrack( idx , ret):
            
            if len(ret) == len(s):
                retbox.append(ret)
            
            else:
                if s[idx].isalpha():
                    backtrack(idx+1 , ret+s[idx].swapcase())
                backtrack(idx+1 , ret +s[idx])
                
        backtrack( 0 , "")
        return retbox 