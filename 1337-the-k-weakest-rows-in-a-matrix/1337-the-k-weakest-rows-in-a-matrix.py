class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        numone = []
        for i, row in enumerate(mat):
            numone.append([i,row.count(1) ])
            
        res = [] 
        for a,b in sorted(numone , key= lambda x:x[1] ):
            res.append(a)
        return res[:k]