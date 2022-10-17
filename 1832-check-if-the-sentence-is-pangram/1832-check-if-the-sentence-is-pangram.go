func checkIfPangram(sentence string) bool {
    
    	for i := 97; i < 123; i++ {
		    if !strings.Contains(sentence, string(i)) {
			return false
		}
	}
	return true
}