func topKFrequent(words []string, k int) []string {
    
    wmap := make(map[string]int , 0)
    var box []string 
    for _, w := range words {
        
        wmap[w] ++  
        if wmap[w] == 1 {
            box = append(box, w)
        }
    }
    
    sort.Slice(box , func(x,y int) bool { 
        if wmap[box[x]] == wmap[box[y]] {
            return box[x] < box[y]
        } else {
            return wmap[box[x]] > wmap[box[y]]
        }
    })
    
    return box[:k] 
}