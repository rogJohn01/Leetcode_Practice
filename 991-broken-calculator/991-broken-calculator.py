class Solution(object):
    def brokenCalc(self, s, k):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """

        if s >k:
            return s-k
        cnt = 0 
        while True:

            if k ==s:
                return cnt 

            if k&1 ==0 and k>s:
                k //=2 
            else: 
                k+=1 

            cnt +=1         