class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        def backtrack(ix , ip , loc ,dot ):

            if ix == len(s):
                if dot ==3:
                    if  loc >=2 and ip[-loc] =="0":
                        return 
                    if 0<= int(ip[-loc:]) <= 255: 
                        ans.append(ip)
                return

            if loc <3: 
                backtrack(ix+1 , ip+s[ix] , loc+1 , dot)

            if loc !=0:
                if  loc >=2 and ip[-loc] =="0":
                    return 

                if 0<= int(ip[-loc:]) <= 255: 
                    backtrack(ix , ip+"." , 0 , dot+1)



        ans = [] 
        backtrack(0,"" ,  0 , 0)
        return ans 