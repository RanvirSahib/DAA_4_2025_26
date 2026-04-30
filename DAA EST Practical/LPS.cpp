#include <bits/stdc++.h>
using namespace std;

int longestPalindromeSubseq(string &s) {
    int n = s.size();
    if (n == 0) return 0;
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int i = n - 1; i >= 0; --i) {
        dp[i][i] = 1;
        for (int j = i + 1; j < n; ++j) {
            if (s[i] == s[j]) {
                dp[i][j] = 2 + (j > i + 1 ? dp[i + 1][j - 1] : 0);
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    return dp[0][n - 1];
}

int main() {
    string s;
    if (!(cin >> s)) return 0;
    cout << longestPalindromeSubseq(s);
    return 0;
}
