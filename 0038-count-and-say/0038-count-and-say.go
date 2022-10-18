func countAndSay(n int) string {
    if n ==1 {
        return "1"
    }
    s := countAndSay(n-1)
    ans := ""
    i := 0 
    for i < len(s) {
        j := i+1 
        for j < len(s) && s[j] == s[i] {
            j ++
        }
    ans += strconv.Itoa(j-i) + string(s[i])
    i = j 
    }
    return ans 
}