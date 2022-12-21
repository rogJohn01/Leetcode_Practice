
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def bfs(source):
            q = deque([source])
            color[source] = 0
            while q:
                node = q.popleft()
                for nnode in graph[node]:
                    if color[nnode] == color[node]: return False
                    if color[nnode] == -1:
                        color[nnode] = 1 - color[node]
                        q.append(nnode)

            return True

        graph = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)
        for i in range(1, n + 1):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True