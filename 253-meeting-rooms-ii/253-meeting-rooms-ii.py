class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        freeRoom = [] 

        intervals.sort(key = lambda x:x[0])

        heapq.heappush(freeRoom , intervals[0][1])

        for i in intervals[1:]:

            if freeRoom[0] <= i[0]:
                heapq.heappop(freeRoom)
            heapq.heappush(freeRoom , i[1])
        return len(freeRoom)