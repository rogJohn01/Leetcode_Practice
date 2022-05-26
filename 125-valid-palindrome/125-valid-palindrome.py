class Solution:
    def isPalindrome(self, s: str) -> bool:
        
          s = ''.join(e for e in s.lower() if e.isalnum())
          return s==s[::-1]