class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        def cal(n):
            return 1 + (n-1)*(0.5*n +1)
        
        
        combo =0 
        ans = 0 
        for n in nums: 
            
            if n ==0: 
                combo +=1 
            else: 
                ans += cal(combo)
                combo =0 
                
        if combo:
            ans += cal(combo)
        
        return int(ans) 
            