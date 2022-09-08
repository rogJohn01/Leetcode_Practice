/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
   
    ans =  []int{}
	dfs(root  ) 
	return ans 
}

var ans []int

func dfs(node *TreeNode ){

	if node != nil {
		
		dfs(node.Left  ) 
		ans = append(ans, node.Val) 
        dfs(node.Right )  		

	}

}
