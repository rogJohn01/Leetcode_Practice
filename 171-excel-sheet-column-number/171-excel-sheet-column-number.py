class Solution:
    def titleToNumber(self, s: str) -> int:
        def cv(s):
            return ord(s)- ord('A') +1

        sco = 0
        d = len(s)
        for i,e in enumerate(s):
            if i != d-1:    
                sco += cv(e)* 26**(d-1-i)
            else:
                sco += cv(e)
        return sco 
