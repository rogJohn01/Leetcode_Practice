class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        dict = defaultdict(int)
        for x in s:
            dict[x] +=1 
        for y in t:
            dict[y] -=1
        
        return all( x==0 for x in dict.values())