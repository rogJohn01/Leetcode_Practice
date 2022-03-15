class Solution:
    def simplifyPath(self, path: str) -> str:


        st = [] 
        for port in path.split('/'):

            if port == '..':
                if st:
                    st.pop()

            elif port == '.' or not port:
                continue 

            else:
                st.append(port)
        return '/'+'/'.join(st)