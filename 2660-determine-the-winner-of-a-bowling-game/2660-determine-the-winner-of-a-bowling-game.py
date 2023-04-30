class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def cal(arr):
            score =0 
            bonus =0 
            for a in arr:
                if a ==10:
                    if bonus: 
                        bonus =2 
                        score += 2*10
                    else:
                        bonus =2
                        score +=10 
                elif bonus: 
                    bonus -=1 
                    score += 2*a
                else: 
                    score +=a 
            return score 
        
        left = cal(player1)
        right = cal(player2)
        print(left , right)
        
        if left > right: 
            return 1
        elif left < right:
            return 2
        else: 
            return 0 
        
        
        
        
        