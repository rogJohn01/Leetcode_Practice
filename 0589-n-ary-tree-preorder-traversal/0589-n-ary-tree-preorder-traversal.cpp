/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    

    vector<int> preorder(Node* root){

        vector<int> ans; 
        if(!root) return ans; 
        stack<Node*> st ; 
        st.push(root) ; 
        while(!st.empty()){
            auto top = st.top() ; 
            st.pop(); 
            ans.push_back(top->val); 
            for(auto it = rbegin(top->children) ; it != rend(top->children) ; it++)
                st.push(*it) ; 
        }
        return ans; 
    }
};