class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], rst: List[int]) -> int:
        
        from collections import defaultdict 
        graph = defaultdict(list)
        seen = set(rst) 
        for x, y in edges:
            if (x in seen) or( y in seen):
                continue 
            graph[x].append(y)
            graph[y].append(x) 
        
        global ans 
        ans =0 
        def dfs(v):
            global ans 
            
            seen.add(v) 
            ans +=1 
            for nv in graph[v]: 
                if nv not in seen: 
                    dfs(nv) 



        
        dfs(0)
        return ans 