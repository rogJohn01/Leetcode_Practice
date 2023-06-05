class Solution:
    def matrixSumQueries(self, n: int, q: List[List[int]]) -> int:


        q.reverse()

        rows = set()
        cols = set()
        ans =0 

        for t, ix , v in q: 

            if t==0 and ix not in rows: 
                ans += v*(n-len(cols))
                rows.add(ix)
            if t==1 and ix not in cols: 
                ans += v*(n-len(rows))
                cols.add(ix)
        return ans 