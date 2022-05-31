class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        import re 
        
        pp = re.compile(p)
        
        if pp.fullmatch(s):
            return True 
        else:
            return False