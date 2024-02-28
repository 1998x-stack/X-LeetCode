#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// 函数：将字符串数组分组为字母异位词
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    // 哈希表，用于存储字母异位词分组
    unordered_map<string, vector<string>> map;
    
    for (string& str : strs) {
        // 对字符串进行排序
        string key = str;
        sort(key.begin(), key.end());
        
        // 将原字符串添加到对应的分组中
        map[key].push_back(str);
    }
    
    // 收集结果
    vector<vector<string>> result;
    for (auto& pair : map) {
        result.push_back(pair.second);
    }
    
    return result;
}

int main() {
    // 示例输入
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    
    // 调用函数，并打印结果
    vector<vector<string>> groups = groupAnagrams(strs);
    for (const auto& group : groups) {
        for (const string& str : group) {
            cout << str << " ";
        }
        cout << endl;
    }
    
    return 0;
}