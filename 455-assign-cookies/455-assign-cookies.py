class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            g.sort()
            s.sort()
            k = 0 
            cnt = 0 
            for s1 in s:
                if k ==len(g):
                    break 

                if s1 >=g[k]:
                    cnt +=1 
                    k +=1 
            return cnt 
