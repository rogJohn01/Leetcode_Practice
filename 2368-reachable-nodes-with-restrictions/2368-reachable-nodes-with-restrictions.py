class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], rst: List[int]) -> int:
        
        from collections import defaultdict 
        graph = defaultdict(list)
        rst = set(rst) 
        for x, y in edges:
            if (x in rst) or( y in rst):
                continue 
            graph[x].append(y)
            graph[y].append(x) 
        
        global ans 
        ans =0 
        def dfs(v):
            global ans 

            visit[v] =1 
            ans +=1 
            for nv in graph[v]: 
                if not visit[nv]: #and nv not in rst: 
                    dfs(nv) 



        visit = [0]*n 
        dfs(0)
        return ans 