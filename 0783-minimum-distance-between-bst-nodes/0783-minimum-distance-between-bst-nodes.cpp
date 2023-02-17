/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> arr ; 
    
    void inorder(TreeNode* node){
        if(node ==NULL) return ; 
        
        
        inorder(node->left) ; 
        arr.push_back(node->val) ; 
        inorder(node->right) ;
    }
    
    
    
    int minDiffInBST(TreeNode* root) {
        
        inorder(root) ;
        int ans = INT_MAX ; 
        for(int i=1 ; i < arr.size() ; i++){
            if( arr[i]-arr[i-1] < ans ) 
                ans = arr[i] -arr[i-1] ; 
        }
        return ans ; 
    }
};