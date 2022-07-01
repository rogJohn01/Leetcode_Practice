class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort( key = lambda x: (-x[1],x[0]))
        
        bxload = uload = 0 
        for bx , un in boxTypes: 
            if bxload < truckSize: 
                if bxload +bx < truckSize: 
                    bxload += bx 
                    uload += bx*un 
                else: 
                    dif = truckSize - bxload 
                    uload += un*dif 
                    break 
    
            else:
                break 
        
        return uload 