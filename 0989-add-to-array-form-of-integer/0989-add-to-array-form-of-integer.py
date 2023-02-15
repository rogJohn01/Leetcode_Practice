class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        sumv = ''.join(map(str,num)) 
        tot = int(sumv) + k 
        return [ int(t) for t in str(tot)]