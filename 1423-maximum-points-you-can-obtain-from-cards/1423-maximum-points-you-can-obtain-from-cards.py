class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        

        prel = []
        pf = 0 
        for n in nums: 
            pf += n
            prel.append(pf)

        prer = [] 
        pf = 0
        for n in nums[::-1]:
            pf +=n 
            prer.append(pf) 

        maxv = 0 
        for i in range(k+1):
            if i ==0: 
                tmp = prer[k-i-1] 
            elif i==k: 
                tmp = prel[i-1] 
            else: 
                tmp = prel[i-1]+prer[k-i-1] 
            maxv = max(maxv ,tmp) 

        return maxv 

