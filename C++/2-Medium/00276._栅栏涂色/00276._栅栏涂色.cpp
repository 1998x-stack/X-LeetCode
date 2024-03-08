#include <iostream>
#include <vector>
using namespace std;

// 函数用于计算涂色的方法数
int numWays(int n, int k) {
    if (n == 0 || k == 0) return 0; // 边界情况处理
    if (n == 1) return k; // 只有一根栅栏时的情况
    int same = 0, diff = k; // 初始化same和diff
    for (int i = 2; i <= n; ++i) { // 从第二根栅栏开始遍历
        int temp = same;
        same = diff; // 更新same
        diff = (temp + diff) * (k - 1); // 更新diff
    }
    return same + diff; // 返回总方法数
}

int main() {
    int n = 3, k = 2; // 示例输入
    cout << "Total ways to paint the fence: " << numWays(n, k) << endl; // 输出结果
    return 0;
}