class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        def dfs(n,g,visited):

            if visited[n]:
                return 
            visited[n] =1
            for x in dic[n]:
                dfs(x,dic,visited)

        visited = [0]*n
        dic = {x: [] for x in range(n)}
        for x,y in edges:
            dic[x].append(y)
            dic[y].append(x)
        ret = 0
        for i in range(n):
            if not visited[i]:
                dfs(i,dic, visited)
                ret +=1 
        return ret 