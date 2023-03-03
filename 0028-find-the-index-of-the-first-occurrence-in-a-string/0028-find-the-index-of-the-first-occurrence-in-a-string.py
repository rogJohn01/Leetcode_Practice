class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        nl = len(needle)
        for i in range(len(haystack)):
            
            if haystack[i:i+nl] == needle:
                return i 
        return -1 
                