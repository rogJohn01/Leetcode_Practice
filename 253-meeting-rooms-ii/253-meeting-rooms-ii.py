class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        start = sorted([e[0] for e in intervals]) 
        end =  sorted([e[1] for e in intervals])

        sp = 0
        ep = 0 
        usedRoom = 0 

        while sp < len(start):

            if start[sp] >= end[ep]:
                usedRoom -=1 
                ep +=1
            usedRoom +=1 
            sp +=1 
        return usedRoom 