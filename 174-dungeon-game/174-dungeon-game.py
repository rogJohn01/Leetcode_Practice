class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        R , C = len(dungeon) , len(dungeon[0])
        dp = [[float('inf')]*C for _ in  range(R)]

        def MinHP(curCell , nRow , nCol):

            if nRow >= R or nCol >=C:
                return float('inf')
            nexCell  = dp[nRow][nCol]

            return max(1, nexCell- curCell)

        for row in reversed(range(R)):
            for col in reversed(range(C)):
                curCell = dungeon[row][col]

                rHP = MinHP(curCell, row ,col+1)
                dHP = MinHP(curCell , row+1 , col)
                nexHP = min(rHP, dHP)

                if nexHP != float('inf'):
                    minHP = nexHP
                else: 
                    minHP = 1 if curCell >=0 else (1- curCell)
                dp[row][col] = minHP
        return dp[0][0]