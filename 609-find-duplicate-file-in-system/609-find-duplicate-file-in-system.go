func findDuplicate(paths []string) [][]string {
    
    cash := map[string][]string {} 
    for _ , path := range paths {
        splits := strings.Split(path , " ")
        base := splits[0] 
        for _, split := range splits[1:] {
            i := strings.Index(split, "(")
            fileName := split[:i]
            cont := split[i+1:] 
            cash[cont] = append( cash[cont] , base+ "/" + fileName)
        }
    }

    ans := make([][]string ,0)
    for _ , v := range cash {
        if len(v) > 1 { 
            ans = append(ans ,v) 
        }
    }
    return ans 
    }


