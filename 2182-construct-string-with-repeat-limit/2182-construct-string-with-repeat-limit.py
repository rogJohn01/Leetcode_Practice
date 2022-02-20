class Solution:
    def repeatLimitedString(self, s: str, limit: int) -> str:
 

        c = Counter(s)
        queue= sorted(c.keys())
        res = ''
        while queue:
            
            x = queue.pop()
            if c[x] <= limit:
                res += x*c[x]
                c[x] = 0 
            else:
                res += limit*x
                c[x] -= limit
                if queue:
                    res +=queue[-1]
                    c[queue[-1]] -=1
                    if c[queue[-1]] ==0:
                        queue.pop()
                    queue.append(x)
        return res 