class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) <10: return
        mp = defaultdict(int) 
        ans = [] 
        for i in range(10,len(s)+1):
            
            subs = s[i-10:i]
            mp[subs] +=1 
            if mp[subs] >=2 and subs not in ans:
                ans.append(subs) 
                
        return ans 
        