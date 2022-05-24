class Solution:
    def reverseParentheses(self, s: str) -> str:
            

        st= [] 
        box = [] 
        ss = [] 
        for i,e in enumerate(s):

            if e=='(':
                st.append(i) 

            elif e==')':
                box.append( [ st.pop() , i] )

            ss.append(e) 

        for l,r in box: 
            ss[l:r] = ss[l:r][::-1] 

        tmp = [] 
        for e in ss:
            if e.isalpha():
                tmp.append(e) 

        return ''.join(tmp)  

