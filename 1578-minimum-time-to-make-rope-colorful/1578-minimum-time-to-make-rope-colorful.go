func minCost(colors string, time []int) int {
    

        ans := 0 
        n := len(colors) 
        l := 0 

        for l < n {
            tcost := 0 
            maxC := 0 
            r := l 
            for r < n && colors[r] == colors[l] {
                tcost += time[r] 
                maxC = max(maxC , time[r] )
                r ++ 
            }
            ans += tcost - maxC 
            l = r 
        }
        return ans 
    
}

 func max(a,b int ) int{ 
            if a > b { 
                return a 
            }
            return b 
        } 
