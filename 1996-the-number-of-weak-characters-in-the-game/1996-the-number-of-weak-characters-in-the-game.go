func numberOfWeakCharacters(prop [][]int) int {
    
    
        sort.Slice( prop , func(i, j int) bool {
            if prop[i][0] == prop[j][0] {
                return prop[i][1] < prop[j][1] 
            }
            return prop[i][0] > prop[j][0] 
        })

        ans := 0 
        maxv := 0 
        for _, v := range prop { 
            if v[1] < maxv {
                ans ++ 
            } else {
                maxv = v[1] 
            }
        }
        return ans 
    }

    
