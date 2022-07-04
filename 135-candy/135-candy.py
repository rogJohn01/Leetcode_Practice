class Solution:
    def candy(self, ra: List[int]) -> int:
        
        ans  = [1]*len(ra)
        for i in range(1,len(ra)): 

            if ra[i-1] < ra[i]: 
                ans[i] = ans[i-1]+1  

        for i in range(len(ra)-1,0,-1):

            if ra[i-1] > ra[i]:
                ans[i-1] = max( ans[i-1] ,ans[i] +1 )

        return sum(ans)