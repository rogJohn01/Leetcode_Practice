/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func hasPathSum(root *TreeNode, tar int) bool {
    
    if root == nil {
        return false 
    }

    if root.Left == nil && root.Right == nil {
        return tar == root.Val
    }
    return hasPathSum(root.Left , tar - root.Val) || hasPathSum(root.Right , tar - root.Val)
    }