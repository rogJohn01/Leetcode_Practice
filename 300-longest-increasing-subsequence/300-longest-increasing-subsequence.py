class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
       


            st = [nums[0]] 
            for n in nums[1:]: 
                
                if st[-1] <n:
                    st.append(n) 

                else: # st[-1] >n 
                    i = 0
                    while st[i] < n:                                             i +=1 
                    st[i] = n
                    
            return len(st)

