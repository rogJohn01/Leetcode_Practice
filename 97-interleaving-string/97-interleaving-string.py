class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) !=len(s3):
            return False 
    

        q = deque()
        q.append((0,0))
        visit = set((0,0))
        while q: 
            x,y = q.popleft() 

            if x+y == len(s3):
                return True 


            if x+1 <=len(s1) and s1[x] ==s3[x+y] and (x+1,y) not in visit: 
                q.append((x+1,y)) 
                visit.add((x+1,y))
            if y+1 <=len(s2) and s2[y] ==s3[x+y] and (x,y+1) not in visit: 
                q.append((x,y+1))
                visit.add((x,y+1))

        return False 
