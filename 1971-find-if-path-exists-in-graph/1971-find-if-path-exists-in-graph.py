class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        global ans 
        ans = False 

        visit = defaultdict(list)
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(v):
            global ans 
            if v==destination:
                ans = True 

            for i in graph[v]:  
                if not visit[(v,i)]:
                    visit[(v,i)] = 1 
                    dfs(i)
            return 

        dfs(source) 
        return ans 

