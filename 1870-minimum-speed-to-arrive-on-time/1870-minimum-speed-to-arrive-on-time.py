class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
            n = len(dist)
            l = 0 ; r = 10 ** 7 + 1
            while l <r:
                speed = (l +r) >>1 
                hourSpent = 0 

                if speed ==0:
                    break 
                hourSpent = dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(n - 1))


                if hourSpent <=hour:
                    r = speed 

                else: # hourSpent > hour 
                    l = speed  +1

            return  -1 if r ==(10 ** 7 + 1)  else r 




