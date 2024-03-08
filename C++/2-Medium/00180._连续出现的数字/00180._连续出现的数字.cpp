#include <iostream>
#include <vector>
#include <unordered_set>
#include <fstream>

using namespace std;

// 函数：找出至少连续出现三次的数字
vector<int> findConsecutiveNumbers(const vector<int>& nums) {
    vector<int> result;
    unordered_set<int> added; // 用于记录已添加到结果中的数字
    int count = 1; // 当前数字连续出现的次数

    // 遍历数字列表
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] == nums[i - 1]) {
            ++count; // 如果当前数字与前一个相同，增加计数
            // 当连续次数达到3次，并且数字尚未被添加到结果中时，添加到结果列表
            if (count == 3 && added.find(nums[i]) == added.end()) {
                result.push_back(nums[i]);
                added.insert(nums[i]); // 标记为已添加
            }
        } else {
            count = 1; // 如果当前数字与前一个不同，重置计数
        }
    }

    return result;
}

int main() {
    // 示例输入
    vector<int> nums = {1, 2, 2, 2, 5, 5, 5, 8};
    // 找出连续出现三次的数字
    vector<int> result = findConsecutiveNumbers(nums);

    // 打印结果
    cout << "连续出现三次的数字有：" << endl;
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    // 保存到本地文件
    ofstream outFile("/mnt/data/consecutive_numbers.cpp");
    if (outFile.is_open()) {
        outFile << "#include <iostream>\n#include <vector>\n#include <unordered_set>\n\nusing namespace std;\n\nvector<int> findConsecutiveNumbers(const vector<int>& nums);\n\nint main() {\n    vector<int> nums = {1, 2, 2, 2, 5, 5, 5, 8};\n    vector<int> result = findConsecutiveNumbers(nums);\n    for (int num : result) {\n        cout << num << \" \";\n    }\n    cout << endl;\n    return 0;\n}\n\n// 实现函数...\n";
        outFile.close();
    }

    return 0;
}
