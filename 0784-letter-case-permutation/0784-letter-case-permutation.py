class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        

        def backtrack(ix , sc  ): 

            if len(sc) == len(s):
                ans.append(sc)
                return 


            if s[ix].isalpha():
                if s[ix].isupper():
                    ss = s[ix].lower() 
                else: 
                    ss = s[ix].upper() 

                backtrack(ix+1 , sc+ss )
            backtrack(ix+1 , sc+s[ix])


        ans = [] 
        backtrack(0, "")
        return ans 