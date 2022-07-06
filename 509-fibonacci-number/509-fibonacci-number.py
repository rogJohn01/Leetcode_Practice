class Solution:
    def fib(self, n: int) -> int:
        
        if n==0:
            return 0 

        pr1 = 0 
        pr2  = 1 
        cur = pr1+pr2 
        for _ in range(n-1):
            pr2 = pr1 
            pr1 = cur 
            cur = pr1 + pr2 
        return cur 