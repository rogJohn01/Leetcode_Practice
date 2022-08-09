class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        

        arr.sort() 
        mod = 10**9+ 7 

        dp = { n:1 for n in arr } 

        for i , n in enumerate(arr): 
            for j in range(i): 
                if  not (n% arr[j]) and ( n// arr[j] ) in dp: 
                    dp[n] += dp[arr[j]]* dp[n// arr[j]]
                    dp[n] %= mod 

        return sum(dp.values()) %mod 