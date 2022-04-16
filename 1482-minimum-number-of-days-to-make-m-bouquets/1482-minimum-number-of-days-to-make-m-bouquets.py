class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        
        
        def checkDay(days , m , k):
                f =0
                for n in bloomDay:
                    if n <=days:
                        f +=1 
                        if f ==k:
                            f =0 
                            m -=1 
                            if not m:
                                return True 
                    else: 
                        f = 0 
                return False 

        l = 1 ; h = 10**9
        while l<h:

            mdays = (l+h) >>1 


            if checkDay(mdays,m,k):
                h = mdays 
            else:
                l = mdays +1 

        return l  if checkDay(h,m,k) else -1 