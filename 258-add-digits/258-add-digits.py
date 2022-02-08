class Solution:
    def addDigits(self, snum: int) -> int:
        
        
        while len(str(snum)) !=1:
        
            snum = [ int(e) for e in str(snum)]
            snum = sum(snum)
        return snum