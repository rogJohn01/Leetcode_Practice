class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # if first customer isn't paying $5 it is false 
        
        # you can also use $10 and $20 dollars bill
        
        # creating test cases is important ! 
        
        coinbox = [] 
        for b in bills: 
            
            if b==5: 
                coinbox.append(5)
                
            if b ==10:
                coinbox.append(10)
                if 5 in coinbox:
                    coinbox.remove(5)
                else: 
                    return False 
            if b == 20:
                coinbox.append(20)
                if (5 in coinbox and 10 in coinbox):
                    coinbox.remove(5)
                    coinbox.remove(10)
                elif coinbox.count(5)  >=3:
                    coinbox.remove(5)
                    coinbox.remove(5)
                    coinbox.remove(5)

                
                
                else: 
                    return False 
                
        return True 