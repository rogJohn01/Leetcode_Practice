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
    
     int[] nums; 
        
     public TreeNode helper(int l ,int r){
        if(l> r) return null ; 

        int p = (l+r) /2 ; 
        if(( l+r) % 2==1 ) p++; 
        
        TreeNode root = new TreeNode(nums[p]) ;
        root.left = helper(l , p-1) ; 
        root.right = helper(p+1 , r) ; 
        return root ; 
    
    }
    
    
    public TreeNode sortedArrayToBST(int[] nums) {
        
        this.nums = nums ; 
        return helper( 0 , nums.length -1 ) ; 
    }
}