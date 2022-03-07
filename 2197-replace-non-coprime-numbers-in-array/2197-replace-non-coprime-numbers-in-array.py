class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
       
            stack = [] 
            for n in nums:
                
                stack.append(n)
                while len(stack)>1 and math.gcd(stack[-1] , stack[-2] ) >1:
                    k = stack.pop()
                    stack.append(math.lcm( k , stack.pop() ) )

            return stack 
