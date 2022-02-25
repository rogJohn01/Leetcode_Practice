class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        R, C = len(rooms), len(rooms[0])

        for r in range(R):
            for c in range(C):
                if rooms[r][c] ==0:
                    queue = deque()
                    for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                        queue.append((r+a,c+b ,1))

                        visited = set()

                        while queue:
                            x, y , v = queue.popleft()
                            if x <0 or x>= R or y<0 or y>=C:
                                continue 
                            if rooms[x][y] in [0,-1] or (x,y) in visited: 
                                continue 
                            visited.add((x,y))
                            rooms[x][y] = min(rooms[x][y] ,v)
                            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                                queue.append((x+a, y+b , v+1 ))