#include <iostream>
#include <string>
#include <vector>
using namespace std;


int numDecodings(string s){
    if(s.empty() || s[0] == '0') return 0;
    int n = s.size();
    vector<int> dp(n+1, 0);
    dp[0] = 1;
    dp[1] = s[0] != '0'? 1 : 0;
    for(int i = 2; i<=n; i++){
        int oneDigit = stoi(s.substr(i-1, 1));
        int twoDigit = stoi(s.substr(i-2, 2));
        if(oneDigit >= 1) dp[i] += dp[i-1];
        if(twoDigit >= 10 && twoDigit <= 26) dp[i] += dp[i-2];
    }
    return dp[n];
}

int main() {
    string s = "226";
    cout << "Number of ways to decode \"" << s << "\": " << numDecodings(s) << endl;
    return 0;
}