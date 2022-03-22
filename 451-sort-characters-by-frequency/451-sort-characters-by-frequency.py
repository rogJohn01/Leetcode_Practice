class Solution:
    def frequencySort(self, s: str) -> str:
        


        cntr = Counter(s)

        heap = [(-v,k) for k ,v in cntr.items()]
        heapq.heapify(heap)

        res = [] 
        while heap:

            v, k = heapq.heappop(heap)
            res += [k]* -v 
        return ''.join(res)