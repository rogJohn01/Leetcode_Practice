class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        

        r1 = len(mat1) ; c1 = len(mat1[0])
        r2 = len(mat2) ; c2 = len(mat2[0])


        ans = [ [0]*c2 for _ in range(r1)]


        for c in range(c2):
            for r in range(r1):
                sumv =0 
                for i in range(c1):
                    sumv += mat1[r][i]*mat2[i][c]

                ans[r][c] = sumv 
        
        return ans 