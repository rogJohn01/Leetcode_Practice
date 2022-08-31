class Solution:
    def pacificAtlantic(self, mat: List[List[int]]) -> List[List[int]]:
            
            
        if not mat or not mat[0]: return []
        m, n = len(mat[0]), len(mat)
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited and mat[dx][dy] >= mat[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))

            return visited

        pacific  = [(0, i) for i in range(m)]   + [(i, 0) for i in range(1,n)]
        atlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]

        return bfs(pacific) & bfs(atlantic)