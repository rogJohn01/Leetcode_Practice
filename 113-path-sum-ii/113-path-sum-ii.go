/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, sum int) [][]int {
    
    
	ans := make([][]int, 0)
	tmp := make([]int ,0) 
	helper(root , sum , &ans , tmp)
	return ans 

}

func helper(root *TreeNode , sum int , ans *[][]int , tmp []int ){
	if root == nil {
		return 
	}
	if root.Left == nil && root.Right == nil && root.Val == sum {
		tmp = append(tmp , root.Val) 
		*ans = append(*ans , append([]int(nil) , tmp...))
	}
	helper(root.Left , sum - root.Val , ans , append(tmp, root.Val))
	helper(root.Right , sum - root.Val , ans , append(tmp, root.Val))
}



