/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func goodNodes(root *TreeNode) int {
        
    ans := 0 
    dfs(root, root.Val , &ans)
    return ans 
}

func dfs(root *TreeNode, val int , ans *int){
    if root ==nil {
        return 
    }
    if root.Val >= val {
        *ans ++ 
    }
    maxv := val 
    if val < root.Val {
        maxv = root.Val 
    }
    dfs(root.Left , maxv , ans )
    dfs(root.Right, maxv , ans )
}

