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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        

        int rtidx = 0; 
        return dfs(preorder,inorder , rtidx ,0 , inorder.size()-1) ; 
    }

    TreeNode* dfs(vector<int>& preorder , vector<int>& inorder, int& rtidx , int l , int r ){
    
        if(l > r) return NULL; 
        int pvt = l ; 
        while( inorder[pvt] != preorder[rtidx]) pvt ++ ; 

        rtidx ++; 
        TreeNode* nnode = new TreeNode(inorder[pvt]); 
        nnode->left = dfs(preorder,inorder , rtidx , l , pvt -1) ; 
        nnode->right = dfs(preorder, inorder, rtidx , pvt +1 ,r ) ; 
        return nnode ; 
}
        
        
        
    
};