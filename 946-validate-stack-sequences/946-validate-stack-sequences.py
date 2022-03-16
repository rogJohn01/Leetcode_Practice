class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
       

        j = 0 
        st = [] 
        for p in pushed:
            st.append(p)
            while st and j < len(popped) and st[-1] ==popped[j]:
                st.pop()
                j +=1 
        
        return len(st) ==0