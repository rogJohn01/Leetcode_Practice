class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort( key = lambda x: (-x[1],x[0]))
        
        bxload = uload = 0 
        for bx , un in boxTypes: 
            if bxload < truckSize: 
                dif = bx  if bxload +bx < truckSize else truckSize - bxload
                bxload += dif 
                uload += dif*un 
                
            else:
                break 
        
        return uload 