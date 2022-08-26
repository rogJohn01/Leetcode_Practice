class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        xcntr = Counter(str(n))
        for a in range(31):
            if xcntr == Counter(str(1 << a)):
                return True 
        return False 