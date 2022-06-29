class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        import heapq as hq 
        hp = [] 
        for p in people:
            hq.heappush(hp ,(-p[0], p[1]))

        ans = [] 
        while hp: 
            p = hq.heappop(hp)
            ans.insert(p[1] , [-p[0], p[1]])
        return ans 