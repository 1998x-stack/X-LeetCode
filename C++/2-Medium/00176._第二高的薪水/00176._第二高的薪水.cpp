#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <climits> // 添加对climits的包含

using namespace std;

// 函数：找到第二高的薪水
int findSecondHighestSalary(vector<int> salaries) {
    if (salaries.size() < 2) return INT_MIN; // 如果少于两个薪水，则返回INT_MIN表示不存在第二高的薪水
    
    // 去重并排序
    sort(salaries.begin(), salaries.end());
    auto last = unique(salaries.begin(), salaries.end());
    salaries.erase(last, salaries.end());
    
    if (salaries.size() < 2) return INT_MIN; // 去重后再次检查
    
    // 返回倒数第二个元素作为第二高的薪水
    return salaries[salaries.size() - 2];
}

int main() {
    // 示例数据
    vector<int> salaries = {300, 200, 200, 100, 100};
    
    // 寻找第二高的薪水
    int secondHighest = findSecondHighestSalary(salaries);
    
    // 输出结果
    if (secondHighest == INT_MIN) {
        cout << "第二高的薪水不存在" << endl;
    } else {
        cout << "第二高的薪水是: " << secondHighest << endl;
    }
    
    return 0;
}