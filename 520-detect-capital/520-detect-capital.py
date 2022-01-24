class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        cnt =0 
        for s in word:
            if s.isupper():
                cnt +=1
                
        if cnt ==len(word):
            return True 
        if cnt ==0:
            return True 
        if word[0].isupper() and cnt ==1:
            return True 
        else:
            False 