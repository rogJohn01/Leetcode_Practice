class Solution:
    def minTimeToType(self, word: str) -> int:
          
            
        ans = len(word)
        prev = 'a'
        for w in word:
            val = (ord(w) - ord(prev)) % 26
            ans += min(val , 26-val )
            prev = w 
        return ans 