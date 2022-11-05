class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s= list(s)
        vl = ['a','A', 'e','E', 'i','I', 'o', 'O' , 'u' ,'U' ]
        key = [] 
        for i ,v in enumerate(s):

            if v in vl:
                key.append(i)

        l , r = 0 ,len(key)-1

        while l< r:

              s[key[l]] , s[key[r]] = s[key[r]] , s[key[l]]
              l +=1 
              r -=1 

        return ''.join(s)
