class Solution {
public:
    int maxLength(vector<int>& ribs, int k) {
    int l = 0, r = accumulate(begin(ribs), end(ribs), 0l) / k;
    while (l < r) {
        int m = (l + r + 1) / 2, obtain = 0;
        for (int i = 0; i < ribs.size() && obtain < k; ++i)
            obtain += ribs[i] / m;
        if (obtain < k)
            r = m - 1;
        else
            l = m;
    }
    return l;
}
};