func removeStones(stones [][]int) int {
    
    N := len(stones)
    parent := make([]int , N)
    for i := 0 ; i < N ; i++ { 
        parent[i] = i 
    }
    
    for r := 0 ; r < N ; r++ {
        for c := 0 ; c < N ; c++ { 
            stn1 , stn2 := stones[r] , stones[c]
            if stn1[0] == stn2[0] || stn1[1] == stn2[1] {
                pr := find(parent, r)
                pc := find(parent ,c)
                parent[pc] = pr 
            }
        }
    }
    
    ans := 0 
    for i := 0 ; i < N ; i++ { 
        if parent[i] == i {
            ans++
        }
    }
    return N-ans 

    
    
    
}


func find(parent []int, ix int) int {
    
    i := ix
    for parent[i] != i {
        i = parent[i]
    }
    parent[ix] = i
    return i
}