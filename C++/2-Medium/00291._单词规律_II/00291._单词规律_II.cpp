#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

bool backtrack(int patIndex, int sIndex, string &pattern, string &s, map<char, string> &m, set<string> &used) {
    if (patIndex == pattern.size() && sIndex == s.size()) return true; // 找到一种映射方式
    if (patIndex >= pattern.size() || sIndex >= s.size()) return false; // 不匹配的情况

    char currentChar = pattern[patIndex];
    for (int i = sIndex; i < s.size(); ++i) {
        string str = s.substr(sIndex, i - sIndex + 1);
        if (m.count(currentChar) && m[currentChar] == str) { // 当前字符已映射且相等
            if (backtrack(patIndex + 1, i + 1, pattern, s, m, used)) return true;
        } else if (!m.count(currentChar) && !used.count(str)) { // 未映射，尝试映射
            m[currentChar] = str;
            used.insert(str);
            if (backtrack(patIndex + 1, i + 1, pattern, s, m, used)) return true;
            m.erase(currentChar); // 回溯
            used.erase(str);
        }
    }
    return false;
}

bool wordPatternMatch(string pattern, string s) {
    map<char, string> m;
    set<string> used;
    return backtrack(0, 0, pattern, s, m, used);
}

int main() {
    string pattern = "abab", s = "redblueredblue";
    cout << (wordPatternMatch(pattern, s) ? "true" : "false") << endl;
    return 0;
}