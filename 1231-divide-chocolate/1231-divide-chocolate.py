class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
     
        
        l = 0 ; r = 1000000000
        while l <r: 

            m = (l+r+1) >>1 

            pre = cnt = 0 
            for sw in sweetness:

                if pre +sw <=m:
                    pre +=sw
                else:
                    pre = 0 
                    cnt +=1 

            if cnt >= k+1:
                l = m 

            else:
                r = m-1 

        return l+1 
