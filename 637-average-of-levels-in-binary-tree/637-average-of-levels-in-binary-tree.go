/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfLevels(root *TreeNode) []float64 {
    
        q := []*TreeNode{ root} 
        ans:= []float64{} 
        for len(q) != 0 { 
            n , sum := len(q), 0
            for i:= 0 ; i< n ; i++ {
                node := q[0]
                q = q[1:] 
                if node.Left != nil {
                    q = append(q , node.Left ) } 
                if node.Right != nil { 
                    q = append(q , node.Right) } 
                sum += node.Val 
            }
            ans = append(ans , float64(sum) / float64(n))
        }
        return ans 
} 
