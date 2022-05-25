class Solution:
    def minSteps(self, s: str, t: str) -> int:
        


        cnt =0 
        arr= [0]*27
        for e in s:
            arr[ord(e)- ord('a') ] +=1 

        for e in t: 
            arr[ord(e) - ord('a') ] -=1 

        return sum( abs(e)   for e in arr )  