/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
    
    	
	ans := make([][]int ,0) 
	dfs(root , 0 , &ans ) 
    return ans 
}

func dfs(root *Node , dep int, ans *[][]int) { 
	if root ==nil { 
		return } 

	if dep+1 > len(*ans) {
		*ans = append(*ans , make([]int,0)) 
	}
	(*ans)[dep] = append((*ans)[dep] , root.Val)
	for i := range root.Children { 
		dfs( root.Children[i] , dep+1 , ans)
	}
}


    
