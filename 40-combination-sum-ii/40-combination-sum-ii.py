class Solution:
    def combinationSum2(self, cand: List[int], target: int) -> List[List[int]]:
            
            
            if sum(cand) < target:
                return 
            if len(cand) >10 and len( Counter(cand).keys()) ==1 and sum(cand) >= target:
                return [list(Counter(cand).keys())*(target//cand[0])]
            
            
            ret = []
            def backtrack( rem , path , cntr, start):


                if rem ==0:
                    path.sort()
                    if path not in ret:
                        ret.append(path[:])

                if rem < 0:
                    return 

                for i in range(start , len(cand)):
                    if cntr[cand[i]] >0 :
                        cntr[cand[i]] -=1
                        backtrack(rem -cand[i] , path+[cand[i]] , cntr, i)
                        cntr[cand[i]] +=1


            backtrack(target , [] , Counter(cand)  ,0  )
            return ret 