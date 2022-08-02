class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        

        R = len(mat) ; C = len(mat[0]) 
        mxhp = [] 
        for r in range(R):
            for c in range(C):
                heappush(mxhp , -mat[r][c] ) 
                if len(mxhp) > k: 
                    heappop(mxhp)

        return -heappop(mxhp) 

