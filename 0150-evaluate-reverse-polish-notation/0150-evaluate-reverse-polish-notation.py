class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        def operator(op):
            b = st.pop()
            a = st.pop() 

            if op=="+":
                st.append(a+b)
            elif op=="-":
                st.append(a-b)
            elif op=="*":
                st.append(a*b)
            else: 
                st.append(int(a/b)) 


        st = [] 
        for t in tokens: 
            if t.isdigit() or len(t)>=2:
                st.append(int(t)) 
            else: 
                operator(t) 

        return st[-1]
