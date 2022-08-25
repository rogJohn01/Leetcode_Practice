func canConstruct(ransomNote string, magazine string) bool {
    
    
    box := make([]int ,26)
    for _,v := range magazine{
        box[v-'a'] ++
    }
    for _,v := range ransomNote{
        box[v-'a']--
        if box[v-'a'] < 0 {
            return false 
        }
    }
    return true 

}