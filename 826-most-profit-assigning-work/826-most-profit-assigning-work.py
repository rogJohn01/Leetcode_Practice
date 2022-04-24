class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        

        info =[] 
        for d ,p in zip(difficulty , profit):
            info.append([ d,p ] ) 

        info.sort( key=lambda x: -x[1] ) 
        worker.sort(reverse = True ) 

        sumv = 0 ; i = 0 
        for d,p in info:

            while i < len(worker) and d <= worker[i]:
                sumv += p
                i +=1

        return sumv 


