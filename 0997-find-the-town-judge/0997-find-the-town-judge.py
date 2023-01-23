class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n==1: return 1
        follower = defaultdict(int)
        followed = defaultdict(int)

        for ix in range(len(trust)):
            follower[trust[ix][0]] +=1 
            followed[trust[ix][1]] +=1 
        for ix in range(1,n+1):
            if followed[ix] == n-1:
                if follower[ix] ==0: 
                    return ix 
        return  -1 




