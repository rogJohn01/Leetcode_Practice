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
    TreeNode* sortedArrayToBST(vector<int>& num) {
        

        if(num.size() ==0) return NULL ; 
        if(num.size() ==1) return new TreeNode(num[0]);

        int m = num.size()/2 ;
        TreeNode* root = new TreeNode(num[m]); 

        vector<int> Left(num.begin() , num.begin()+m); 
        vector<int> Right(num.begin()+m+1 , num.end()); 

        root->left = sortedArrayToBST(Left) ; 
        root->right = sortedArrayToBST(Right); 

        return root ; 
        
        
    }
};