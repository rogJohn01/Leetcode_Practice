class Solution:
    def minTimeToType(self, word: str) -> int:
            al = [] 
            alp = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(len(word)):

                    if i ==0:
                        k1 = abs( alp.index(word[i]) - alp.index('a') )
                        k2 = abs( - alp.index(word[i]) + alp.index('a') )
                        if k2 >0:
                            k2 = 26 -k2 
                        ans = min( k1 , k2) 
                        al.append(ans )
                    else: 
                        k1 = abs( alp.index(word[i]) - alp.index(word[i-1]) )
                        k2 = abs( - alp.index(word[i]) + alp.index(word[i-1]) )
                        if k2 >0:
                            k2 = 26 -k2 
                        ans = min( k1 , k2) 
                        al.append(ans )

            return   sum(al) + len(al)
