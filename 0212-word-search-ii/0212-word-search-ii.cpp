struct TrieNode {
    TrieNode* chdr[26] = {}; 
    string* word;
    
    void addWord(string& word){
        TrieNode* cur = this; 
        for(char c: word){
            c -= 'a'; 
            if (cur->chdr[c]==nullptr) {
                cur->chdr[c] = new TrieNode();
                }
            cur = cur->chdr[c];
        }
        cur->word= &word; 
            
        }
    };



class Solution {
public:
    
    int R, C; ; 
    int dir[5] = {0,1,0,-1,0};
    vector<string> ans; 
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        
        R = board.size() ; C = board[0].size(); 
        TrieNode trieNode; 
        for(string& w :words) trieNode.addWord(w);
        
        for(int r=0 ; r < R; r++){
            for(int c=0; c < C; c++){
                dfs(board, r,c , &trieNode);
            }
        } 
        return ans; 
    }
    
    void dfs(vector<vector<char>>& board , int r ,int c , TrieNode* cur){
         if (r < 0 || r == R || c < 0 || c == C || board[r][c] == '#' || cur->chdr[board[r][c]-'a'] == nullptr) return;
        char tmp = board[r][c] ;
        cur = cur->chdr[tmp-'a'];
        if( cur->word != nullptr){
            ans.push_back(*cur->word);
            cur->word = nullptr ; 
        }
        board[r][c] = '#' ; 
        for(int i=0; i< 4 ; i++){
            dfs(board,r+dir[i], c+dir[i+1], cur); 
        }
        board[r][c] = tmp; 
    
    }
};