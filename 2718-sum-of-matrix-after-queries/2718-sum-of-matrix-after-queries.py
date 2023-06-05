class Solution:
    def matrixSumQueries(self, n: int, q: List[List[int]]) -> int:
        
        q.reverse()
        rows = set()
        cols = set()
        ans = 0
        
        for t, i, v in q:
            if t == 0 and i not in cols:
                ans += v * (n - len(rows))
                cols.add(i)
            
            if t == 1 and i not in rows:
                ans += v * (n - len(cols))
                rows.add(i)
                
        return ans