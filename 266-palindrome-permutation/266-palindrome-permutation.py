class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        

        dic = {}
        
        for e in s:
            
            if e in dic:
                dic[e] +=1
            else: 
                dic[e] =1
        
        cnt = 0 
        for key in dic:
            
            if dic[key] % 2 ==1:
                
                cnt +=1 
        
        
        return  cnt <2