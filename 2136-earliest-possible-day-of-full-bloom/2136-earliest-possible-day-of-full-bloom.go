func earliestFullBloom(plantTime []int, growTime []int) int {
      n := len(growTime)
    ixs := make([]int, n)
    
    for i := range ixs {
        ixs[i] = i
    }
    
    sort.Slice(ixs, func(i, j int) bool {
        return growTime[ixs[i]] > growTime[ixs[j]]
    })
    
    plant, ans := 0, 0
    
    for _, ix := range ixs {
        plant += plantTime[ix]
        ans = max(ans, plant + growTime[ix])
    }
    
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}