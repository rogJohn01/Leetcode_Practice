func findOriginalArray(changed []int) []int {
 
    
    

        if len(changed) % 2 != 0 { 
            return []int{} 
        }

        sort.Ints(changed) 

        dic := make(map[int]int) 
        for _, v := range changed {
            dic[v] ++ 
        }

        res := []int{} 

        for _, val := range changed {
            cnt := dic[val] 
            if cnt > 0 { 
                dic[val]--
                tmp := val*2 
                if v, tr := dic[tmp] ; tr { 
                    if v > 0 {
                        res = append(res ,val)
                        dic[tmp] -- 
                    }else {
                        return []int{} 
                    }
                }else { 
                    return []int{}
                }
            }
        }
        return res 
    }
    
    
