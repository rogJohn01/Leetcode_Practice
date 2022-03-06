class Solution:
    def dayOfTheWeek(self, day: int, m: int, year: int) -> str:
        
        def yearCount(year): 
            sy = 1971 
            leap = 0 
            for i in range(sy ,year):
                if i % 400==0 or (i %100 !=0 and i%4 ==0):
                    leap +=1 
            return 365*(year-sy) + leap 

        sd= 5
        dic = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if ( year % 400 ==0 ) or ( year % 4 ==0 and year % 100 !=0):
            days[1] = 29

        date = day+sum(days[:m-1])+	 yearCount(year)
        return  dic[ (date+sd) % 7-1 ]
