class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        cnt =0 
        
        prevEnd = 0
        for _ , end in intervals:
            
            if end > prevEnd:
                cnt +=1 
                prevEnd = end 
        return cnt 