/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int sm = min(p->val,q->val) ;
        int big =max(p->val, q->val) ; 
        
        while(root !=nullptr){
            if(root->val > big) root = root->left ;
            else if(root->val <sm) root = root->right ;
            else return root ; 
        }
        return nullptr ; 
    }
};