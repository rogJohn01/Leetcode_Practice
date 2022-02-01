class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        pre = 0
        maxv = -float('inf')
        ret = [] 
        for i in range(len(gain)):
            ret.append(pre)
            pre += gain[i]
        ret.append(pre)
        return  max(ret) 