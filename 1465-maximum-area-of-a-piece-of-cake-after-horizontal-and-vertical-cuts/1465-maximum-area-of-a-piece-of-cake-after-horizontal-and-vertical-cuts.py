class Solution:
    def maxArea(self, h: int, w: int, hcut: List[int], vcut: List[int]) -> int:

        mod = 10**9 + 7
        hcut.insert(0,0)
        hcut.append(h) 

        vcut.insert(0,0)
        vcut.append(w) 
    
        hcut.sort() ; vcut.sort() 
        maxh = maxv = 0 
        for i in range(1,len(hcut)):
                 maxh = max ( maxh ,( hcut[i]- hcut[i-1] ))

        for i in range(1, len(vcut)): 
            maxv = max(maxv , ( vcut[i] - vcut[i-1] )) 

        return maxv*maxh %(mod)
