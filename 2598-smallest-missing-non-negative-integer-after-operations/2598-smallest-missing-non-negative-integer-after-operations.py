class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        


        dic = defaultdict(int) 

        for n in nums: 
            dic[n%value] +=1 

        i =-1 
        while True: 
            i +=1 
            if (i % value ) in dic and dic[i%value] >0:
                dic[i%value] -=1 
            else: 
                break
        return i