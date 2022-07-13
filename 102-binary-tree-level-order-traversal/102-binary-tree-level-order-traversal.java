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
    public List<List<Integer>> levelOrder(TreeNode root) {
        

        List<List<Integer>> ans = new ArrayList<>(); 
        if( root == null) return ans; 
        Queue<TreeNode> queue = new LinkedList<>(); 
        queue.add(root) ; 
        while( !queue.isEmpty()) { 
            List<Integer> dep = new ArrayList<>(); 
            int cnt = queue.size() ; 
            for(int i=0 ; i< cnt ; i++){
                TreeNode node = queue.poll() ; 
                dep.add(node.val) ; 
                if( node.left != null) queue.add(node.left) ; 
                if( node.right!= null) queue.add(node.right) ; 
            }
            ans.add(dep) ;
        }
        return ans ; 
        
        
    }
}