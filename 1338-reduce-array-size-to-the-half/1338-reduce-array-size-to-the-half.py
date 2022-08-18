class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        fs = len(arr)
        cntr = Counter(arr) 
        ans = tmp = 0 
        for n in sorted(cntr.values() , key= lambda x:-x):
            ans +=1 
            tmp += n
            if tmp >= fs/2:
                return ans 

        return ans 