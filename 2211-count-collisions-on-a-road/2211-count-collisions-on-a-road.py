class Solution:
    def countCollisions(self, dir: str) -> int:



        right =0 ; res = 0 ; obstacle = False 

        for d in dir:

            if d=='R':
                right +=1 
            elif d=='S':
                res += right 
                right = 0 
                obstacle = True 

            else: # d=='L'
                if right > 0:
                    res += right +1 
                    right = 0 
                    obstacle = True 
                elif obstacle:
                    res +=1

        return res 