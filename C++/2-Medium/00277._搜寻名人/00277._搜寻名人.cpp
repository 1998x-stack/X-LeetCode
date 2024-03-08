#include <iostream>
#include <vector>
using namespace std;

// 假设的 knows API
bool knows(int a, int b);

class Solution {
public:
    // 寻找名人
    int findCelebrity(int n) {
        int candidate = 0;
        // 第一次遍历，找出可能的名人
        for (int i = 1; i < n; i++) {
            if (knows(candidate, i)) {
                candidate = i;
            }
        }
        
        // 第二次遍历，验证这个人是否真的是名人
        for (int i = 0; i < n; i++) {
            if (i != candidate && (knows(candidate, i) || !knows(i, candidate))) {
                return -1; // 不满足名人条件
            }
        }
        return candidate; // 返回名人编号
    }
};

// knows API 实现，此处为占位符
bool knows(int a, int b) {
    // 实际使用时，这里会有具体实现
    return true; // 假设返回值
}

int main() {
    // 示例，创建Solution实例并调用findCelebrity方法
    Solution solution;
    int n = 3; // 假设聚会中有3个人
    int celebrity = solution.findCelebrity(n);
    cout << "The celebrity is: " << celebrity << endl;
    return 0;
}