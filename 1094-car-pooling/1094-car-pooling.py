class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        timestamp = [] 
        for trip in trips:
            
            timestamp.append( [trip[1], trip[0]])
            timestamp.append([trip[2] , -trip[0]])
        
        timestamp.sort()
        currpass = 0
        for time , passenger in timestamp:
            currpass += passenger
            
            if currpass > capacity:
                return False 
        return True 
            
            
            
            