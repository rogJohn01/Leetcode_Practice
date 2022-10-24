func maxLength(arr []string) int {
    

    c := []uint32{}
    ans := 0 
    for _ , s := range arr { 
        var mask uint32
        for _ , c := range s { 
            mask = mask | 1 << (c-'a')
        }
        if len(s) != bits.OnesCount32(mask) {
            continue }
        c = append(c, mask)
    }
    dfs(c, 0, 0, &ans)
    return ans 
    }


func dfs(c []uint32 , ix int , mask uint32 , ans *int){

        *ans = Max(*ans , bits.OnesCount32(mask))
        for i := ix ; i < len(c); i++ { 
            if mask & c[i] == 0 { 
                dfs(c , i+1 , mask | c[i] , ans)
            }
        }
        return 
    }

func Max(a,b int) int{ 
        if a > b { 
            return a } 
    return b 
    }
