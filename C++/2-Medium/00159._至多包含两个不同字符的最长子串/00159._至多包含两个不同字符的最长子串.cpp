#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> freq; // 字符出现频率表
        int maxLen = 0; // 最长子串的长度
        int left = 0; // 滑动窗口左边界
        for (int right = 0; right < s.length(); ++right) {
            freq[s[right]]++; // 将右边界字符加入频率表

            // 如果窗口中的不同字符超过2个，则移动左边界直到不同字符数为2
            while (freq.size() > 2) {
                freq[s[left]]--; // 左边界字符出现频率减1
                if (freq[s[left]] == 0) {
                    freq.erase(s[left]); // 如果字符出现频率为0，则从表中删除该字符
                }
                left++; // 移动左边界
            }

            // 更新最长子串长度
            maxLen = max(maxLen, right - left + 1);
        }
        return maxLen;
    }
};

int main() {
    Solution solution;
    string s = "eceba";
    cout << "The length of the longest substring with at most two distinct characters is: "
         << solution.lengthOfLongestSubstringTwoDistinct(s) << endl;
    return 0;
}