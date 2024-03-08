#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

// 计算字符串的特征
string getFeature(const string& str) {
    string feature;
    for (int i = 1; i < str.size(); ++i) {
        int diff = str[i] - str[0];
        if (diff < 0) diff += 26; // 处理循环移位
        feature += to_string(diff) + ' '; // 构建特征字符串
    }
    return feature;
}

// 主函数
int main() {
    vector<string> strings = {"abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"};
    unordered_map<string, vector<string>> groups;

    // 遍历字符串数组，根据特征归组
    for (const auto& str : strings) {
        string feature = getFeature(str);
        groups[feature].push_back(str);
    }

    // 输出分组结果
    for (const auto& group : groups) {
        for (const auto& str : group.second) {
            cout << str << " ";
        }
        cout << endl;
    }

    return 0;
}