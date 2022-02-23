class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        R, C= len(rooms), len(rooms[0])

        for i in range(R):
            for j in range(C):
                if rooms[i][j] ==0:
                    queue = deque()
                    for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                        queue.append((i+a,j+b , 1))

                        visited = set() 
                        while queue:
                            x,y , val = queue.popleft()
                            if x < 0 or y < 0 or x >= R or y >=C:
                                continue 
                            if rooms[x][y] in [0,-1] or (x,y) in visited:
                                continue 
                            visited.add((x,y))
                            rooms[x][y] = min(rooms[x][y] ,val)
                            for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                                queue.append((x+a,y+b , val+1))

