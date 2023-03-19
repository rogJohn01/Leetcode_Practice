class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        s = bin(n)[2:][::-1]

        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] == "1":
                if i % 2 ==0: 
                    a+=1 
                else:
                    b+=1 
        return [a,b]

