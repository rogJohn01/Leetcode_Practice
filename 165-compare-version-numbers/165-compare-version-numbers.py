class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
            
            from itertools import zip_longest
            v1 ,v2 = list(map(int, v1.split('.'))) , list(map(int, v2.split('.')))
            for r1,r2 in zip_longest(v1,v2 , fillvalue=0):
                if r1 ==r2:
                    continue 
                else:
                    return -1 if r1 < r2 else 1 

            return 0 
