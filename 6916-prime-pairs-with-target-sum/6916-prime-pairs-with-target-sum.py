class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        
        
        def helper(n):
            primes = [True for i in range(n+1)]
            p = 2
            while p * p <= n:
                if primes[p] == True:
                    for i in range(p * p, n+1, p):
                        primes[i] = False
                p += 1
            prime_numbers = [p for p in range(2, n) if primes[p]]
            return prime_numbers

        primes =  helper(n)


        l = 0 ; r = len(primes) -1 
        ans = [] 
        while l <= r: 

            sumv = primes[l] + primes[r]
            if sumv ==n:
                ans.append([ primes[l] , primes[r]])
                l+=1
            elif sumv < n: 
                l +=1 
            else: 
                r -=1 

        return ans 