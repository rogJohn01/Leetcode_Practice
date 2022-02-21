class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        


        ls1 = len(s1)
        ls2 = len(s2)

        s1alp = 26*[0]
        s2alp = 26*[0]


        for s in s1:
            s1alp[ord(s)- ord('a')] +=1 

        for i in range(ls2):

            s2alp[ord(s2[i]) - ord('a')] +=1

            if i>=ls1:
                s2alp[ord(s2[i-ls1]) - ord('a')] -=1 
            if s1alp ==s2alp:
                return True 
        return False  


    