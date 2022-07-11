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
    vector<int> rightSideView(TreeNode* root) {
        
        vector<int> ans; 
        dfs(root ,0,ans); 
        return ans; 

    }
        
void dfs(TreeNode* root, int dep, vector<int> &ans){
    if(!root) return ; 
    if(dep >= ans.size()) ans.push_back(root->val); 
    dfs(root->right , dep+1,ans); 
    dfs(root->left , dep+1 ,ans); 


        
    }
};