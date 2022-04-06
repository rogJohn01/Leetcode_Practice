class Solution:
    def dailyTemperatures(self, tem: List[int]) -> List[int]:
    
    
    
        lt= len(tem)
        ans = [0]*lt
        st = []
        for i in range(lt):

            while st and tem[st[-1]] < tem[i]:
                k = st.pop()
                ans[k] = i-k 
            st.append(i)
        return ans 