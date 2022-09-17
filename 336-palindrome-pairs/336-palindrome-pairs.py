class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        

        def check_pal(w):
           return w == w[::-1]

        words = { w:i for i,w in enumerate(words)}
        valid = [] 
        for word , k in words.items(): 
            ln = len(word)
            for j in range(ln+1): 
                prf = word[:j]
                suf = word[j:]
                if check_pal(prf):
                    back = suf[::-1] 
                    if back != word and back in words: 
                        valid.append([words[back] , k])
                if j != ln and check_pal(suf):
                    back = prf[::-1]
                    if back != word and back in words:
                        valid.append( [ k, words[back]] )
        return valid 