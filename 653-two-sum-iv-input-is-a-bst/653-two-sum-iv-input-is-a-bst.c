/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void traverse(struct TreeNode* root, int *arr, int *idx){ 

    if(!root) return ; 
    traverse( root->left, arr, idx) ; 
    arr[(*idx)++ ] = root->val; 
    traverse( root->right , arr , idx) ; 
}


bool findTarget(struct TreeNode* root, int k){

    
        
    int *arr = malloc(sizeof(int)*10000) , idx = 0 , sumv=0 ; 
    traverse(root, arr , &idx) ; 
    int i,j ; 
    for(i=0 ,j=idx-1; i<j; ){

        sumv = arr[i]+arr[j] ; 
        if(sumv > k) j  -- ; 
        else if(sumv < k) i++ ; 
        else break ; 
    }
    return i==j? false:true ; 

}