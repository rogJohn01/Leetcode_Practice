class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

            xhr = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings])

            ans, mxheap = [[0, 0]], [(0, float('inf'))]
            for x, negh, R in xhr:
                while x >= mxheap[0][1]:

                    heapq.heappop(mxheap)
                if negh:

                    heapq.heappush(mxheap, (negh, R))
                curmxh = -mxheap[0][0]
                if ans[-1][1] != curmxh:
                    ans.append([x, curmxh])
            return ans[1:]