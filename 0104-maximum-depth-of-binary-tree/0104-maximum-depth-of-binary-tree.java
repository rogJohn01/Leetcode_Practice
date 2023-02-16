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
    public int maxDepth(TreeNode node) {
        LinkedList<TreeNode> st = new LinkedList<>() ; 
        LinkedList<Integer> depths = new LinkedList<>() ; 
        if(node == null) return 0 ; 
        
        st.add(node) ; 
        depths.add(1) ;
        
        int ans = 0 , dep = 0 ; 
        while(!st.isEmpty()){
            node = st.pollLast() ;
            dep = depths.pollLast() ; 
            if(node!= null){
                ans = Math.max(ans , dep ) ; 
                st.add(node.left) ; 
                st.add(node.right) ; 
                depths.add(dep+1) ; 
                depths.add(dep+1) ; 
            }
        }
        return ans ; 
    }
}