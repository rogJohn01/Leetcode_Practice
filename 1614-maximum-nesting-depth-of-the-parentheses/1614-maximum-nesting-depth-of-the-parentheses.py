class Solution:
    def maxDepth(self, s: str) -> int:
        


        st = []
        maxl = 0 
        for e in s: 

            if e=='(':

                st.append(e)
                if len(st) > maxl:
                    maxl = len(st) 

            elif e==')':
                if st: 
                    st.pop() 
                    
                    
        return maxl 

