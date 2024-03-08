#include <iostream>
#include <string>
using namespace std;

// 判断是否只有一个编辑距离
bool isOneEditDistance(string s, string t) {
    int m = s.length(), n = t.length();
    if(abs(m-n)>1) return false;
    int count = 0;
    int i = 0, j = 0;
    while (i < m && j < n) {
        if (s[i] != t[j]) {
            if (count == 1) return false;
            if (m > n) i++;
            else if (m < n) j++;
            else {
                i++;
                j++;
            }
            count++;
        } else {
            i++;
            j++;
        }
    }

    if (i < m || j < n) count++;
    return count == 1;
}

int main() {
    string s = "ab", t = "acb";
    cout << (isOneEditDistance(s, t) ? "true" : "false") << endl;
    return 0;
}