
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int dep) {
        if (dep == 0 || dep == 1) {
            TreeNode* nroot = new TreeNode(val);
            (dep ? nroot->left : nroot->right) = root;
            return nroot;
        }
        if (root && dep >= 2) {
            root->left  = addOneRow(root->left,  val, dep > 2 ? dep - 1 : 1);
            root->right = addOneRow(root->right, val, dep > 2 ? dep - 1 : 0);
        }
        return root;
    }
};