class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        pre = 0
        maxv = -float('inf')
        ret = [0]
        for i in range(len(gain)):
            pre += gain[i]
            ret.append(pre)

        #et.append(pre)
        return  max(ret) 