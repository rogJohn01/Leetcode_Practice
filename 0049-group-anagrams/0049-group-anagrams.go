func groupAnagrams(strs []string) [][]string {
    
    mp := map[[26]int][]string{}
    for _ , s := range strs {
        char := [26]int{}
        for _ ,c := range s { 
                char[c-'a']++
            }
            mp[char] = append( mp[char] , s )
        }
        
        ans := [][]string{}
        for _ ,v := range mp { 
            ans = append( ans ,v )
        }
        return ans 
    }
