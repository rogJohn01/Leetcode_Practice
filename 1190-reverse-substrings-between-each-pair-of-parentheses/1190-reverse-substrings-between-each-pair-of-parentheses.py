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

        def twopointer(l,r,s):

            while l <r: 
                s[l] , s[r] = s[r] , s[l] 
                l +=1 ; r -=1 

            return s 

        for l,r in box: 
            twopointer(l,r,ss) 

        tmp = [] 
        for e in ss:
            if e.isalpha():
                tmp.append(e) 

        return ''.join(tmp) 

        