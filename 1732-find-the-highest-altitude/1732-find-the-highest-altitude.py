class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        pre = 0
        maxv = 0 
        ret = [0]
        for i in range(len(gain)):
            pre += gain[i]
            maxv = max(maxv , pre)

        #et.append(pre)
        return  maxv