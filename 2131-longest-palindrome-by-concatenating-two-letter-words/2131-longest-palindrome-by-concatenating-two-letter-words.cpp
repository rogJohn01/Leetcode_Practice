class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        
    vector<vector<int>> cntr(26, vector<int>(26, 0));
    int ans = 0;
    for (string w: words) {
        int a = w[0] - 'a', b = w[1] - 'a';
        if (cntr[b][a]) ans += 4, cntr[b][a]--;
        else cntr[a][b]++;
    }
    for (int i = 0; i < 26; i++) {
        if (cntr[i][i]) {
            ans += 2;
            break;
        }
    }
    return ans;
}
    
};