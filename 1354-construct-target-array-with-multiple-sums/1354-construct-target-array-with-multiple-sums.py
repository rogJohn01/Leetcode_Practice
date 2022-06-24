class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        import heapq as hq 
        if len(target) ==1:
            return target == [1] 

        sumv = sum(target) 
        box = [ -n for n in target ] 
        hq.heapify(box)

        while -box[0] >1: 
            maxv = -box[0] 
            rest = sumv - maxv
            if rest ==1:
                return True 
            x = maxv % rest 
            if x ==0 or x ==maxv: 
                return False 
            hq.heapreplace(box , -x) 
            sumv -= (maxv-x)
        return True 