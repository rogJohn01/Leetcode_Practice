
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        
        st = [] 
        s = [ e for e in s]
        for i in range(len(s)):

            if s[i] =='(':
                st.append(i)
            if s[i] == ')':

                if st:
                    st.pop()
                else:
                    s[i] = '#'

        while st:
            s[st.pop()] = '#'

        s = ''.join(s)
        s = s.replace('#','')
        return s