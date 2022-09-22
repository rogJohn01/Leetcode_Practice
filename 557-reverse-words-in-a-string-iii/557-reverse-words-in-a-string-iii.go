func reverseWords(s string) string {
    

	ss := strings.Split(s, " ")
	ans := ""
	for i, v := range ss {
		v1 := Reverse(v)
        if i == len(ss)-1 {
            return ans +v1 
        }
        ans += v1 + " "
	}
	return ans 
}

func Reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}