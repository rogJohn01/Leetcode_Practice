class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        

        ans = [] 
        for word in words: 

            dic = {} 
            rdic = {} 
            jp = False 
            for i,p in enumerate(pattern): 


                if word[i] in rdic and rdic[word[i]] !=p:
                    jp = True 
                    break 

                if p  in dic: 
                    if  dic[p] != word[i]:
                        jp = True 
                        break 
                else: 
                    dic[p] = word[i] 
                    rdic[word[i]] = p
            if not jp:
                ans.append(word) 

        return ans 

