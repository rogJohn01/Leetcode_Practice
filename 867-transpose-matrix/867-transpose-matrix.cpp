class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& mat) {



        int M = mat.size() , N = mat[0].size();
        vector<vector<int>> ans(N, vector<int>(M,0));
        for (int j =0; j < N; j++)
            for (int i =0 ; i < M; i++)
                ans[j][i] = mat[i][j];

        return ans; 
    }
};