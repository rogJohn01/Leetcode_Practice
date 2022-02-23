class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        
         if len(fl) ==1:
            return 1-fl[0] >=n 
       

           
         fcnt = 0 
         for i in range( len(fl)-1):

            if fl[0] ==0 and fl[1]==0:
                fcnt +=1 
                fl[0] =1  

            if  i > 0 and fl[i-1] ==0 and fl[i] ==0 and fl[i+1] ==0: 
                 fcnt +=1 
                 fl[i] =1 
            elif  fl[i-1] ==1 and fl[i] ==0 and i+1 ==len(fl)-1 and fl[i+1]==0: 
                 fcnt +=1 
                 fl[i] =1 
         print(fcnt)
         return fcnt  >=n