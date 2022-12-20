class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(v):

            for i in rooms[v]:
                if not record[i]:
                    record[i] =1 
                    dfs(i)

        record= [0]*len(rooms)
        record[0] =1 
        dfs(0)
        for r in record:
            if not r:
                return False 
        return True 