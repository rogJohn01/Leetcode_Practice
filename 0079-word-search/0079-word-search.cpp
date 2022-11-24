class Solution {
public:

    bool dfs(int x, int y , int cnt , vector<vector<char>>& board,string word){
        if(word.length()==cnt) return true ; 

        if( x<0 || x>=board.size() || y<0 || y>=board[0].size() || board[x][y] != word[cnt]) return false ; 

        char tmp = board[x][y];
        board[x][y] = ' ';

        bool ans = dfs(x-1,y ,cnt+1 , board, word) ||
                   dfs(x+1,y ,cnt+1 , board , word) ||
                   dfs(x,y-1 , cnt+1 , board, word) ||
                   dfs(x,y+1, cnt+1 , board, word) ;
        board[x][y] = tmp; 
        return ans; 
    }


    bool exist(vector<vector<char>>& board, string word) {
        int R = board.size(); 
        int C = board[0].size(); 

        for(int r =0 ; r< R ; r++){
            for(int c=0 ; c < C ; c++){
                if(board[r][c] == word[0] && dfs(r,c,0,board, word)){
                    return true ; 
                }
            }
        }
        return false; 
    }
};

