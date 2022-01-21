class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d1 , d2 = [] , [] 
        for i , v in enumerate(wordsDict):

            if v == word1:
                d1.append(i)
            if v == word2:
                d2.append(i)
        minv = sys.maxsize
        for e1 in d1:
            for e2 in d2:
                 minv = min(abs(e1-e2) , minv)

        return minv