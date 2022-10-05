/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func addOneRow(root *TreeNode, val int, dep int) *TreeNode {
    

    if dep == 1 {
        return &TreeNode{ val , root , nil }
    }
    q := []*TreeNode{root}
    for { 
        n := len(q)
        if dep ==2 {
            for i:= 0 ; i < n ; i++ { 
                pop := q[0]
                q = q[1:] 
                left , right := pop.Left , pop.Right 
                pop.Left , pop.Right = &TreeNode{ val, left , nil }, &TreeNode{ val , nil , right } 
            }
            break 
        } else { 
            for  i:= 0 ; i < n ; i++ { 
                pop := q[0] 
                q = q[1:] 
                if pop.Left != nil { q = append(q ,pop.Left ) } 
                if pop.Right != nil { q = append( q , pop.Right ) } 
            }
            dep -- 
        }
    }
    return root 

    
    
}