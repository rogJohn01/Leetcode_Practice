

func equationsPossible(equations []string) bool {
    root := [26]int{}
	for i := 0; i < 26; i++ { root[i] = i }
    
    for _, eq := range equations {
        if eq[1] == '=' {
			xroot := find(&root, int(eq[0] - 'a'))
			yroot := find(&root, int(eq[3] - 'a'))
            root[yroot] = xroot
        }
    }
	for _, eq := range equations {
		if eq[1] == '!' {
			xroot := find(&root, int(eq[0] - 'a'))
			yroot := find(&root, int(eq[3] - 'a'))
			if xroot == yroot {
				return false
			}
		}
	}
    return true
}

func find(root *[26]int, x int) int {
	if x != (*root)[x] {
		(*root)[x] = find(root, (*root)[x])
	}
    return (*root)[x]
}