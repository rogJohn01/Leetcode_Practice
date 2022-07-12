class Solution:
    def makesquare(self, msk: List[int]) -> bool:
        
           

            N = len(msk)
            box, rem = divmod(sum(msk), 4)
            if rem or max(msk) > box: return False

            @lru_cache(None)
            def dfs(mask):
                if mask == 0: return 0
                for j in range(N):
                    if mask & 1<<j:
                        tmp = dfs(mask ^ 1<<j)
                        if tmp >= 0 and tmp + msk[j] <= box:
                            return (tmp + msk[j]) % box
                return -1

            return dfs((1<<N) - 1) == 0