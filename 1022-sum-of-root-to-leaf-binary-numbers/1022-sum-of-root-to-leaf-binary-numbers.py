# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        


        tot = 0 
        st = [[root,str(root.val)]] 

        while st: 
            node , path = st.pop()

            if not node.left and not node.right: 

                tot += int(path , 2) 

            if node.left: 
                st.append( [ node.left , path+str(node.left.val) ] ) 
            if node.right:
                st.append( [ node.right , path+ str(node.right.val) ] ) 

        return tot 
