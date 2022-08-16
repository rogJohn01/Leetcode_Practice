class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        first = defaultdict(int)
        inf = float('inf')
        for i,e in enumerate(s): 
            
            if e in first: first[e] = inf 
            else:  first[e] = i 
            
        return min(first.values()) if min(first.values()) != inf else -1 
            
            