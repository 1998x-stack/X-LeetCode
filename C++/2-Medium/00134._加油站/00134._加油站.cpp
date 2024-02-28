#include <iostream>
#include <vector>
using namespace std;

// 函数声明
int canCompleteCircuit(vector<int>& gas, vector<int>& cost);

int main() {
    // 示例输入
    vector<int> gas = {1,2,3,4,5};
    vector<int> cost = {3,4,5,1,2};

    // 调用函数计算结果
    int start = canCompleteCircuit(gas, cost);

    // 输出结果
    cout << "Start from station: " << start << endl;

    return 0;
}

// 函数定义
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int totalTank = 0, currTank = 0, startingStation = 0;
    for (int i = 0; i < gas.size(); i++) {
        int netGain = gas[i] - cost[i];
        totalTank += netGain;
        currTank += netGain;
        // 如果当前油量小于0，重置起始加油站和当前油量
        if (currTank < 0) {
            startingStation = i + 1;
            currTank = 0;
        }
    }
    // 如果总油量大于等于0，返回起始加油站；否则，返回-1
    return totalTank >= 0 ? startingStation : -1;
}