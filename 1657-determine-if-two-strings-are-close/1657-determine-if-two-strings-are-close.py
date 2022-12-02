class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:


        cntr1 = Counter(word1) 
        cntr2 = Counter(word2) 
        
        bool1 = set(cntr1.keys()) == set(cntr2.keys())
        bool2 =  sorted(list(cntr1.values())) == sorted(list(cntr2.values())) 
        return bool1 & bool2 