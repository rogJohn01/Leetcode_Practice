class Solution:
    def merge(self, inter: List[List[int]]) -> List[List[int]]:
        

        inter.sort(  key = lambda x: (x[0] , x[1])) 
        li = len(inter) 
        #if li==1:
         #   return inter
        cs , ce = inter[0] 

        nx =1 
        ans = [[cs,ce]] 
        while nx < li: 

            ns , ne = inter[nx] 

            if ce >= ns and ce <ne: 
                ans.pop() 
                ans.append( [ cs , ne ] ) 
                cs , ce = cs , ne 

            elif ( cs <= ns and ne <= ce ):
                    ans.pop() 
                    ans.append( [cs, ce ] ) 
                    cs , ce  = cs , ce 
            elif ( ns <= cs and ce <= ne):
                    ans.pop() 
                    ans.append( [ ns, ne ] ) 
                    cs , ce  = ns , ne 

            elif ce <=  ns: 
                ans.append( [ns ,ne ] ) 
                cs ,ce = ns , ne 

            nx +=1 

        return ans 