
bool canHarvest(vector<int>& bDay, int harvestDay, int m, int k) {
    int adjacent = 0;
    for (auto bloomDay : bDay) {
        adjacent = bloomDay <= harvestDay ? adjacent + 1 : 0;
        if (adjacent == k) {
            adjacent = 0;
            --m;
        }
    }
    return m <= 0;
}
int minDays(vector<int>& bDay, int m, int k) {
    if (m * k > bDay.size())
        return -1;
    auto lo = 1, hi = 1000000000;
    while (lo < hi) {
        auto mid = (hi + lo) / 2;
        if (canHarvest(bDay, mid, m, k))
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}





#include <iostream>
# 



class Solution {
public:
    vector<string> letterCasePermutation(string S) {
        vector<string> ans;
        backtrack(S, 0, ans);
        return ans;
    }
    
    void backtrack(string &s, int i, vector<string> &ans) {
        if (i == s.size()) {
            ans.push_back(s);
            return;
        }
        // save initial value
        char c = s[i];
        // path1: toggle lower/upper case
        s[i] = islower(c) ? toupper(c) : tolower(c);
        backtrack(s, i + 1, ans);
        // path2: reset back(NOT go to this path if c is digit)
        if (isalpha(c)) {
            s[i] = c;
            backtrack(s, i + 1, ans);
        }
    }
};

