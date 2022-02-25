class Solution:
    def numRescueBoats(self, people: List[int], k: int) -> int:
        
        # try to use two pointer for adding/prefix sum !! 
        
            people.sort()
            l , r = 0 ,len(people)-1
            ant = 0
            while l <=r:
                ant +=1 
                if people[l]+people[r] <=k:
                    l+=1 
                r -=1 
            return ant 