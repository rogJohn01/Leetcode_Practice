class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
       
        dic = {} 
        start = maxl = 0 
        for i, e in enumerate(s):
            if e in dic and  start <= dic[e]:
                start = dic[e] +1 
            else:
                maxl = max(maxl , i-start +1 ) 
            dic[e] = i 

        return maxl 
