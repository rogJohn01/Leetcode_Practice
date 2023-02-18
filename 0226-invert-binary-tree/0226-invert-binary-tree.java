/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        
        if(root == null) {
            return null ; 
        }
        
        final Deque<TreeNode> st = new LinkedList<>() ; 
        st.push(root) ; 
        
        while(!st.isEmpty()) {
            final TreeNode node = st.pop() ; 
            final TreeNode left = node.left ; 
            node.left = node.right ; 
            node.right = left ; 
            
            if(node.left != null){
                st.push(node.left) ; 
            }
            if(node.right != null){
                st.push(node.right) ; 
            }
        }
        return root ; 
    }
}