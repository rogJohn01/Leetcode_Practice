class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        
        wBox = Counter(words)
        wl , nw  = len(words[0]) , len(words) 
        tl , ans = wl*nw , [] 

        for i in range(len(s)-tl+1): 

            seen = defaultdict(int) 
            for j in range(i ,i+tl , wl): 
                cword = s[j:j+wl] 
                if cword in wBox: 
                    seen[cword] +=1 
                    if seen[cword] > wBox[cword]: 
                        break 
                else: 
                    break 
            if seen == wBox: 
                ans.append(i) 
        return ans 