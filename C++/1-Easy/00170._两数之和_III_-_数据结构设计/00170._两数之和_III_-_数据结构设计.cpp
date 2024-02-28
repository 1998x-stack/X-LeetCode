#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class TwoSum {
public:
    unordered_map<int, int> num_counts; // 存储数值及其出现的次数

    // 添加数值到数据结构
    void add(int number) {
        ++num_counts[number];
    }

    // 查找是否存在两个数的和为指定值
    bool find(int value) {
        for (auto& pair : num_counts) {
            int complement = value - pair.first;
            if ((complement != pair.first && num_counts.count(complement)) ||
                (complement == pair.first && pair.second > 1)) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    // 示例操作
    TwoSum ts;
    ts.add(1);
    ts.add(3);
    ts.add(5);
    cout << (ts.find(4) ? "true" : "false") << endl; // 应输出 true
    cout << (ts.find(7) ? "true" : "false") << endl; // 应输出 true
    cout << (ts.find(2) ? "true" : "false") << endl; // 应输出 false
    return 0;
}