class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        cntr = Counter()
        for ww in words2:
            cntr |= Counter(ww)
            
        return [word for word in words1 if not cntr - Counter(word)]
