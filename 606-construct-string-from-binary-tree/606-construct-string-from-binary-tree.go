/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func tree2str(root *TreeNode) string {
    
    if root == nil { return  ""}
    s:= strconv.Itoa(root.Val)
    l:= tree2str(root.Left)
    r:= tree2str(root.Right)
    
    if root.Left == nil && root.Right == nil {
        return s 
    }
    if root.Right == nil { 
        return s+ "(" + l+ ")"
    }
    
    return s+ "(" + l + ")" + "(" + r+ ")"
}