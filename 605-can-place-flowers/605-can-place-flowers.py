class Solution:
    def canPlaceFlowers(self, fl: List[int], k: int) -> bool:
        
       
            cnt =0 
            for i in range(len(fl)):

                if fl[i] ==0:

                    el = (i==0) or fl[i-1] ==0
                    er =  (i == len(fl)-1) or fl[i+1] ==0 

                    if el and er:
                        fl[i] =1
                        cnt +=1 
                        if cnt >=k:
                            return True 
            return cnt >=k