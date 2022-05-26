class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def shift(s):
            s = s+s[0]
            s = s[1:]
            return s

        for _ in range(len(s)):

            s = shift(s)

            if s ==goal:
                return True 

        return False 