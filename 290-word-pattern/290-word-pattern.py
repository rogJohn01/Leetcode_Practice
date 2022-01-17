class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split()):
            return False 
        
        dic = collections.defaultdict()
        for e1, e2 in zip(pattern,s.split()):

            if e1 in dic:
                if dic[e1] != e2:
                    return False 
            dic[e1] = e2 
        
        if len(dic.values()) != len(set(dic.values())):
            return False 
      
        return True 