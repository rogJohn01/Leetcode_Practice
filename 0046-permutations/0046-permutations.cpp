class Solution {
public:
    vector<vector<int>> permute(vector<int>& num) {
    vector<vector<int>> ans ; 

    backtrack(num , 0 , ans) ;
    return ans ; 
}

void backtrack(vector<int> &num , int start , vector<vector<int>> &ans){
    if(start >= num.size()){
        ans.push_back(num) ;
        return ; 
    }

    for(int i= start ; i < num.size() ;i++){
        swap(num[start] , num[i] ) ; 
        backtrack(num , start +1 , ans) ; 
         swap(num[start], num[i]);
    }
}



    
};