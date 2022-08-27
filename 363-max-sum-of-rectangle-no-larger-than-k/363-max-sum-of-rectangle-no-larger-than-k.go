func maxSumSubmatrix(mat [][]int, k int) int {


	R, C := len(mat) , len(mat[0] )
	mxsum := math.MinInt32 

	for i:=0 ; i < R ; i++ { 
		for j:=1 ; j < C ; j++ { 
			mat[i][j] += mat[i][j-1] 
		} } 
	
	for l:=0 ; l < C ; l++ { 
		for r:= l ; r < C ; r++ { 
			prefxs , set := 0 , Set{0} 
			for i:=0 ; i < R ; i++{ 
				sum := mat[i][r] 
				if l > 0 { 
					sum -= mat[i][l-1] 
				}
				prefxs += sum 
				idx := sort.SearchInts(set , prefxs - k )
				if idx != len(set) { 
                    mxsum = max(mxsum , prefxs - set[idx] )
				}
				set.Insert(prefxs) 
			}}}
		return mxsum 
	}

	type Set []int 

	func (s *Set) Insert(x int) {
        i := sort.SearchInts(*s, x)
        if i == len(*s) {
            *s = append(*s, x)
        } else if (*s)[i] != x {
            *s = append(*s, 0)
            copy((*s)[i+1:], (*s)[i:])
            (*s)[i] = x
        }
    }

    func max(a,b int ) int { 
        if a < b { 
            return b 
        }
        return a 
    }
