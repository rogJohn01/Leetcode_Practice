class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
     
        k +=1 
        l = min(sweetness) ; r= sum(sweetness)//k 
        while l <r: 

            m = (l+r+1) >>1 

            pre = cnt = 0 
            for sw in sweetness:

                if pre +sw <m:
                    pre +=sw
                else:
                    pre = 0 
                    cnt +=1 

            if cnt >= k:
                l = m 

            else:
                r = m-1 

        return l 
