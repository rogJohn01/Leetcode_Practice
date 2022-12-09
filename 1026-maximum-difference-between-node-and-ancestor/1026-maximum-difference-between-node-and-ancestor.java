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
    int ans = 0; 
    public int maxAncestorDiff(TreeNode root) {
      
        if(root ==null ) return 0; 
        dfs(root , root.val , root.val ); 
        return ans ; 
    }
    private void dfs(TreeNode node , int min , int max){
        if(node == null) return ; 
        min = Math.min(node.val , min) ; 
        max = Math.max(node.val , max) ; 
        ans = Math.max(ans, max-min) ; 
        dfs(node.left , min , max) ;
        dfs(node.right , min , max) ; 
    }
}